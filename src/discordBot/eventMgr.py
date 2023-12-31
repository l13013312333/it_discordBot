import datetime as dt
import re

import discord
from discord.ext import commands
import src.discordBot.schedule as ScheduleMgr


def _init(client):
  # event 事件處理
  @client.event
  async def on_ready():
    print(f"「{client.user}」已登入")
    ScheduleMgr._init(client)
    

  @client.event
  async def on_connect():
    if client.auto_sync_commands:
      await client.sync_commands()
      print(f"{client.user.name} connected.")

  @client.event
  async def on_message(message):
    if message.author == client.user:  # 排除機器人本身的訊息
      return
    # 純文字偵測「ping」
    if message.content == 'ping':
      await message.channel.send('pong')  # 發送訊息到目標伺服器的文字頻道
    # 偵測機器人被Tag
    elif re.findall(f"<@{client.application_id}>", message.content):
      await message.reply("安安 找我嗎~")  # 使用「回覆」目標訊息
    # 文字判斷
    elif re.findall("呼叫幫手", message.content):
      newStr = message.content.split('呼叫幫手')
      msg = "私訊你囉~ 你剛剛說: " + newStr[1] if len(newStr) > 1 and newStr[1] else "私訊你囉~ "
      await message.author.send(msg)  # 發送訊息到目標成員私訊
    await client.process_commands(message)

  
  @client.event
  async def on_message_edit(before, after):

    authorM = before.author.mention
    channelM = before.channel.mention

    embed = discord.Embed(color=0x34495E, timestamp=dt.datetime.utcnow())
    embed.description = f"{authorM} 在 {channelM} 編輯了訊息"
    embed.add_field(name="編輯前",
                    value=f"``{before.clean_content}``",
                    inline=False)
    embed.add_field(name="編輯後", value=f"``{after.clean_content}``")
    embed.set_author(name="訊息編輯紀錄")
    guild = client.get_guild(before.guild.id)
    await guild.system_channel.send(embed=embed, silent=True)
    return

  @client.event
  async def on_message_delete(message):

    authorM = message.author.mention
    channelM = message.channel.mention

    embed = discord.Embed(color=0x748191, timestamp=dt.datetime.utcnow())
    embed.description = f"{authorM} 在 {channelM} 刪除了訊息"
    embed.add_field(name="刪除的內容", value=f"``{message.content}``")
    embed.set_author(name="訊息刪除紀錄")
    guild = client.get_guild(message.guild.id)
    await guild.system_channel.send(embed=embed, silent=True)
    return

  
  @client.event
  async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.author.send("你沒有權限喔www不可以偷偷來")
    elif isinstance(error, commands.BotMissingPermissions):
      await ctx.author.send("你沒有權限喔www不可以偷偷來Bot")
    elif isinstance(error, commands.NotOwner):
      await ctx.author.send("你沒有權限喔www不可以偷偷來")


  @client.event
  async def on_raw_reaction_add(payload):
        # print(payload.message_id)
        # print(payload.guild_id)
        # print(payload.channel_id)
        # print(payload.emoji.name)
        # print(payload.emoji.id)
        # print(payload.event_type) #REACTION_ADD
        # print(payload.member.nick)
        # print(payload.data)
        guild = client.get_guild(int(payload.guild_id))
        channel = guild.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.data["message_id"])
        # print(message.reactions)



