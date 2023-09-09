# 導入 套件
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import src.discordBot.eventMgr as EventMgr
import src.discordBot.commandMgr as CommandMgr

# 取得環境設定
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
# intents
intents = discord.Intents.default()
intents.message_content = True
# client
client = commands.Bot(command_prefix="$", intents=intents, strip_after_prefix=True)


class DiscordBot:
    def __init__(self) -> None:
        EventMgr._init(client)
        CommandMgr._init(client)
        pass

    def start(self):
        client.run(DISCORD_TOKEN)
