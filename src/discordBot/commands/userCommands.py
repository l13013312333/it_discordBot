
import discord
import datetime as dt

def main(Bot):
	name = "成員指令"
	print(f"{name} 註冊成功")
	
	@Bot.user_command(name="加入伺服器時間", description="計算加入伺服器的時間" )
	async def count_user_joinDays(ctx, member: discord.Member):
		# await ctx.respond(f'用戶命令觸發: {member.joined_at}')
		today = dt.datetime.utcnow()
		joinDay = member.joined_at.replace(tzinfo=None)
		countDays = (today - joinDay).days
		countSecs = (today - joinDay).seconds
		countMins = countSecs // 60
		countHours = countMins // 60

		embed = discord.Embed(color=0x34495E)
		embed.set_author(name=member.display_name, icon_url=member.display_avatar)
		embed.title = f"已加入伺服器 {f'{countDays}天' if countDays else (f'{countHours}時' if countHours else f'{countMins}分')} "

		await ctx.send_response(embed=embed)
