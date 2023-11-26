@bot.listen('on_message') 
async def stuff(message):

    if message.content.startswith("buttlerprefix"): # this tells the bot what to listen for. If a user types `buttlerprefix` in any text channel, it will respond with what's below
        msg = await message.channel.send("my prefix is `>`") # set the sending message equal to a variable so that you can manipulate it later like I did with the timer, and delete function below
        await asyncio.sleep(10) # tells the bot to wait 10 seconds before continuing below
        await msg.delete() # deletes the send message after 10 seconds
