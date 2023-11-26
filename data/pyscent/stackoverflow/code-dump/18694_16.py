async def _check_channel(self, message, pool):
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(
                "SELECT ignore_channel_id FROM guild_channel_settings WHERE guild_id = %s",
                (message.author.guild.id,),
            )
            in_database = await cursor.fetchone()

    if in_database and in_database[0] is not None:
        channel_list = in_database[0].split(" ")
        for channelid in channel_list:

            try:
                channel_id_int = int(channelid)
            except ValueError:
                continue

            if int(message.channel.id) == channel_id_int:
                return False


async def _get_role_count(self, message, pool):
    async with pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(
                "SELECT ignore_role_id, bonus_role_id FROM guild_role_settings WHERE guild_id = %s",
                (message.author.guild.id,),
            )
            in_database = await cursor.fetchone()
    if in_database:
        first_item, second_item, *_ = in_database
        if first_item is not None:
            role_list = first_item.split(" ")
            for roleid in role_list:
                try:
                    roleid_int = int(roleid)
                except ValueError:
                    continue

                role = message.author.guild.get_role(roleid_int)
                if role is None:
                    continue
                if role in message.author.roles:
                    return False

        if second_item is not None:
            role_list = second_item.split(" ")
            count = 0
            for roleid in role_list:
                try:
                    roleid_int = int(roleid)
                except ValueError:
                    continue

                role = message.author.guild.get_role(roleid_int)
                if role is None:
                    continue
                if role in message.author.roles:
                    count += 1
            return count


@commands.Cog.listener("on_message")
async def on_message(self, message):
    if message.author.bot:
        return
    if message.type != discord.MessageType.default:
        return
    if isinstance(message.channel, discord.channel.DMChannel):
        return

    # Cooldown

    self.member_cooldown_list = [
        i
        for i in self.member_cooldown_list
        if i[1] + self.cooldown_val > int(time.time())
    ]
    member_index = next(
        (
            i
            for i, v in enumerate(self.member_cooldown_list)
            if v[0] == message.author.id
        ),
        None,
    )
    if member_index is not None:
        if self.member_cooldown_list[member_index][1] + self.cooldown_val > int(
            time.time()
        ):
            return

    self.member_cooldown_list.append((message.author.id, int(time.time())))

    loop = asyncio.get_running_loop()
    db_pool = await aiomysql.create_pool(
        minsize=3,
        host="<host>",
        port=3306,
        user="<user>",
        password="<password>",
        db="<db_name>",
        autocommit=False,
        loop=loop,
    )
    count = 1

    check_channel_task = asyncio.create_task(
        self._check_channel(self, message, db_pool)
    )
    role_count_task = asyncio.create_task(self._get_role_count(self, message, db_pool))

    # write to database

    mydb = await db_pool.acquire()
    mycursor = await mydb.cursor()
    await mycursor.execute(
        "SELECT * FROM guild_message_count WHERE guild_id = %s AND user_id = %s",
        (message.author.guild.id, message.author.id),
    )
    in_database = await mycursor.fetchone()

    role_count = await role_count_task
    check_channel = await check_channel_task
    if False in (role_count, check_channel):
        await mycursor.close()
        db_pool.release(mydb)
        db_pool.close()
        await db_pool.wait_closed()
        return
    if role_count:
        count += role_count
    if in_database:
        await mycursor.execute(
            "INSERT INTO guild_message_count (user_id, message_count, guild_id) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE message_count = message_count + 1",
            (message.author.id, count, message.author.guild.id),
        )

    await mydb.commit()
    await mycursor.close()
    db_pool.release(mydb)
    db_pool.close()
    await db_pool.wait_closed()
