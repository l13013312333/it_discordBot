
import discord

def main(Bot):
	name = "訊息指令"
	print(f"{name} 註冊成功")
	
	@Bot.message_command(name="訊息ID",description="取得訊息ID")
	async def get_message_id(ctx, message: discord.Message):
		await ctx.respond(f"訊息命令觸發: `{message.id}`")