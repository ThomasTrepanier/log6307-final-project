import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType

bot = commands.Bot(command_prefix=prefix, description="Desc", help_command=None)

@bot.event
async def on_ready():
    DiscordComponents(bot, change_discord_methods=True)
    await bot.change_presence(activity=discord.Game(name=f"{prefix}help"))
    print("Bot has successfully logged in as: {}".format(bot.user))
    print("Bot ID: {}\n".format(bot.user.id))

@bot.command()
async def button(ctx):
    await ctx.send(type=InteractionType.ChannelMessageWithSource, content="Message Here", components=[Button(style=ButtonStyle.URL, label="Example Invite Button", url="https://google.com"), Button(style=ButtonStyle.blue, label="Default Button", custom_id="button")])

bot.run("token")
