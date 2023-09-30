import os
import json
import urllib.request
from src.googleAppSheet import app_sheet_find


async def refresh(Bot):
  selector = f"FILTER('設定檔',([功能名稱] = 'Youtube人數', [功能開關] = true, [排程] = true))" 
  resultStr = app_sheet_find("設定檔", selector)
  result = json.loads(resultStr)

  for data in result:
    guild = Bot.get_guild(int(data["伺服器"]))
    if guild is not None:
      loadChannel = json.loads(data["設定"])
      loadYTID = loadChannel["頻道ID"]
      loadChannelID = loadChannel["伺服器ID"]
      channel = guild.get_channel(loadChannelID)
      await channel.edit(name=get_youtube_subscribers(loadYTID))

      print(f'{loadChannelID}YT頻道文字已更新')


def get_youtube_subscribers(channelID):
  data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels/?part=statistics&id="+channelID+"&key="+os.getenv("SECRET_KEY")).read()
  subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
  
  return f'YouTube 訂閱人數: {subs}'
