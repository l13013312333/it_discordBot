import discord
from discord.ext import commands
from src.googleAppSheet import app_sheet_find, app_sheet_add

import moment
import json


def main(Bot):
    name = "簽到"
    print(f"{name} 註冊成功")

    def check_in_data(member):
      try:
        now = moment.now().timezone("Asia/Taipei")
        selector = f"FILTER('checkIn',([_ComputedKey] = '{str(member.id)}: {now.format('MM/DD/YYYY')}'))"
        resultStr = app_sheet_find("checkIn", selector)

        result = json.loads(resultStr)
        if (len(result) > 0):
          return "你今天已經簽到過了喔w😚"
        else :
          app_sheet_add("checkIn", {
            "ID": str(member.id),
            "日期": moment.now().format("YYYY/MM/DD"),
            "時間": moment.now().format("YYYY/MM/DD HH:mm:ss"),
            "暱稱": member.display_name
          })
          return "簽到成功✅"
      except:
        return "⚠️簽到失敗，請通知管理員處理"


    # 會員功能
    @Bot.command(name=name)
    async def check_in_form_command(ctx):
      await ctx.send(check_in_data(ctx.author))
    
    @Bot.slash_command(name=name, description="成員簽到")
    async def check_in_from_slash_command(ctx):
      await ctx.respond(check_in_data(ctx.author))

  

    # 管理員功能
    @Bot.user_command(name="簽到資訊", description="顯示該成員的簽到資訊")
    @commands.has_permissions(administrator=True)
    @commands.is_owner() # 管理員才能用
    @commands.guild_only() # 伺服器專用
    async def get_member_info(ctx, member: discord.Member):
      await ctx.send_response("功能處理", ephemeral=True)

    @get_member_info.error
    async def get_member_info_error(ctx, error):
      print(error)
      if isinstance(error, commands.NoPrivateMessage):
        await ctx.send_response("這個只能在伺服器裡才能用", ephemeral=True)
      else:
        await ctx.send_response("你沒有權限喔www不可以偷偷來", ephemeral=True)


    @Bot.command(name="簽到資訊")
    @commands.is_owner() # 管理員才能用
    @commands.guild_only()
    async def get_member_info_command(ctx: commands.Context):
      if (ctx.can_send()):
        await ctx.author.send("已上傳")