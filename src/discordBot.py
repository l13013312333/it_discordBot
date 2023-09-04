# 導入 套件
import discord
import os
from dotenv import load_dotenv

# 取得環境設定
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
# intents
intents = discord.Intents.default()
intents.message_content = True
# client
client = discord.Client(intents=intents)

class DiscordBot():
  def __init__(self) -> None:
    pass

  def start(self):
    client.run(DISCORD_TOKEN)


# event 事件處理
@client.event
async def on_ready():
  print(f"「{client.user}」已登入")

@client.event
async def on_message(message):
  print(message) # 印出message 內容
  if message.author == client.user: # 排除機器人本身的訊息
    return
  if message.content == 'ping':
    await message.channel.send('pong')
