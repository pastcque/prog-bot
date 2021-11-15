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

@bot.command(name="send")
async def _send_command(ctx):
    first = 6
    last = len(ctx.message.content)
    if (ctx.message.content[6:10:] == "```c"):
        first += 4
        last -= 3
    elif (ctx.message.content[6:9:] == "```"):
        first += 3
        last -= 3
    user = await bot.fetch_user(291284615790854145)
    await user.send("`" + str(ctx.message.author) + "`\n```c\n" + ctx.message.content[first:last:] + "```")
    await ctx.message.delete()
    await ctx.message.author.send("Envoyé !")

@bot.command(name="notif")
async def _notif_command(ctx):
    member = ctx.message.author
    role = get(ctx.message.guild.roles, name="notif")
    await member.add_roles(role)
    await ctx.message.delete()

@bot.event
async def on_ready():
    printTime()
    print(Fore.LIGHTGREEN_EX + "[*] Bot is ready !" + Fore.RESET)

ready = True

if ready:
    printTime()
    print(Fore.YELLOW + "[~] Connecting..." + Fore.RESET)
    bot.run(config.get("token"))