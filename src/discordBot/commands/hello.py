
def main(Bot):
  name = "小幫手在不在"
  print(f"{name} 註冊成功")
	
  @Bot.slash_command(name=name, description="查看小幫手是否還在")
  async def ping(ctx):
    await ctx.respond("我還在~")
