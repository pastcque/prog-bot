import discord
import json
import time
import os

from colorama import Fore
from discord.ext import commands
from discord.utils import *

botversion = "v1.0"

ready = False

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

with open("./config.json") as file:
    config = json.load(file)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def printTime():
    print(Fore.LIGHTBLUE_EX + time.strftime("%H:%M:%S ", time.localtime()) + Fore.RESET, end="")



# Bannière
banner ="""
Prog bot
--------
- Pstq -
"""
cls()
print(Fore.CYAN + banner + Fore.RESET)

@bot.event
async def on_message(message):
    await bot.process_commands(message)

"""
@bot.command(name="annonce")
async def _annonce_command(ctx):
    embed=discord.Embed(title="Comment envoyer ton code ?", description="Utilise la commande `!send` suivi de ton code\n\nDans le salon <#909457162030448680>")
    embed.set_author(name="Explications", icon_url="https://media4.giphy.com/media/d8tN2ZVaB3ycmYypG5/giphy.gif?cid=790b7611fa0f26ba7851352c77cb99522aaef140d6e3cb5d&rid=giphy.gif&ct=g")
    embed.set_footer(text="Bonne chance !")
    await ctx.send(embed=embed)"""

#  291284615790854145

@bot.command(name="send")
async def _send_command(ctx):
    user = await bot.fetch_user(291284615790854145)
    await user.send("`" + str(ctx.message.author) + "`\n```" + ctx.message.content[5::] + "```")
    await ctx.message.delete()
    await ctx.message.author.send("Envoyé !")

@bot.event
async def on_ready():
    printTime()
    print(Fore.LIGHTGREEN_EX + "[*] Bot is ready !" + Fore.RESET)

ready = True

if ready:
    printTime()
    print(Fore.YELLOW + "[~] Connecting..." + Fore.RESET)
    bot.run(config.get("token"))