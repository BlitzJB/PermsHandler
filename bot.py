from discord.ext import commands
from permshandler import PermsHandler

bot = commands.Bot(command_prefix="!")
perms = PermsHandler()


@bot.event
async def on_ready():
    print("logged in")


@bot.command(pass_context=True)
@perms.check("IA")
async def sus(ctx):
    # Only triggers if user has perms of IA group or higher
    await ctx.send("wow")


bot.run("Token")
