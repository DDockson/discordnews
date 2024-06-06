import discord
from discord.ext import commands
import json
import asyncio
import os

with open("token.json", 'r', encoding='utf-8') as f:
    config = json.load(f)
token = config["token"] #token.json에서 토큰을 가져온다

intents = discord.Intents.default()
intents.message_content = False

bot = commands.Bot(command_prefix="!",intents = intents) #봇의 prefix 설정

async def load():
    for filename in os.listdir("./commands"):
        if filename.endswith("py"):
            await bot.load_extension(f"commands.{filename[:-3]}") #commands 폴더에 있는 명령어들을 불러옴

@bot.event
async def on_ready():
    print('Ready!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="뉴스")) #봇의 상태메시지 설정
    await bot.tree.sync()

asyncio.run(load())

bot.run(token)