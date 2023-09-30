
from discord.ext import tasks
import src.discordBot.schedule.youtube as yt_channel

def _init(Bot):
  
  @tasks.loop(minutes=1)
  async def running():
      await yt_channel.refresh(Bot)

  running.start()
