import os
import json
import urllib.request

import discord
from discord.ext import commands
from discord.commands import Option
from src.googleAppSheet import app_sheet_find, app_sheet_add, app_sheet_edit


def main(Bot):
    name = "建立YT人數頻道"
    print(f"{name} 註冊成功")

  
    @Bot.slash_command(name="channel_yt", description="建立YT人數頻道")
    @commands.has_permissions(administrator=True)
    @commands.is_owner() # 管理員才能用
    @commands.guild_only() # 伺服器專用
    async def create_channel(ctx, channelID: Option(str, "輸入頻道編號", name="頻道編號", required=True)):
      
        try:
            guild = Bot.get_guild(ctx.guild.id) 
            loadSetting = find_setting_data(guild.id)

            if loadSetting is not None:
                loadChannel = json.loads(loadSetting["設定"])
                loadYTID = loadChannel["頻道ID"]
                loadChannelID = loadChannel["伺服器ID"]
                channel = guild.get_channel(loadChannelID)
                await channel.edit(name=get_youtube_subscribers(loadYTID))
                await ctx.respond("已更新完成", ephemeral=True)
            else :
                channel = await guild.create_voice_channel(get_youtube_subscribers(channelID), overwrites={ctx.guild.default_role: discord.PermissionOverwrite(connect=False)})
                in_setting_data('add', ctx.guild.id, channelID, channel.id)
                await ctx.respond("新增完成", ephemeral=True)
                                  
        except Exception as errors:
            print(f"Bot Error: {errors}")
            await ctx.respond("發生錯誤: " + errors, ephemeral=True)
  
    @create_channel.error
    async def info_error(ctx, error):
        await ctx.send_response("你沒有權限喔www不可以偷偷來", ephemeral=True)


def get_youtube_subscribers(channelID):
  data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels/?part=statistics&id="+channelID+"&key="+os.getenv("SECRET_KEY")).read()
  subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
  
  return f'YouTube 訂閱人數: {subs}'


def find_setting_data(guildID):
  selector = f"FILTER('設定檔', ([_ComputedKey] = '{str(guildID)}: Youtube人數'))"
  resultStr = app_sheet_find("設定檔", selector)
  result = json.loads(resultStr)
  if (len(result) > 0):
    return result[0]
  else : 
    return None


def in_setting_data(type, guildID, YTchannelID, channleID):
  data = {
    "伺服器": guildID,
    "功能名稱": "Youtube人數",
    "功能開關": True,
    "排程": True,
    "設定": json.dumps({
      "頻道ID": YTchannelID,
      "伺服器ID": channleID
    }, ensure_ascii=False)
  }
  if type == "edit":
    app_sheet_edit("設定檔", data)
  else :
    app_sheet_add("設定檔", data)