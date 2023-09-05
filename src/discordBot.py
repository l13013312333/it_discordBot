# 導入 套件
import discord
import os
import re
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
  if message.author == client.user: # 排除機器人本身的訊息
    return

  # 純文字偵測「ping」
  if message.content == 'ping':
    await message.channel.send('pong')  # 發送訊息到目標伺服器的文字頻道
  # 偵測機器人被Tag
  elif re.findall(f"<@{client.application_id}>", message.content):
    await message.reply("安安 找我嗎~") # 使用「回覆」目標訊息
	# 文字判斷
  elif re.findall("呼叫幫手", message.content):
    newStr = message.content.split('呼叫幫手')
    msg = "私訊你囉~ 你剛剛說: "+ newStr[1] if len(newStr) > 1 and newStr[1] else "私訊你囉~ "
    await message.author.send(msg) # 發送訊息到目標成員私訊
