import discord
from discord.commands import Option


def main(Bot):
    name = "貼圖反應"
    print(f"{name} 註冊成功")
    emojis = {1: "1️⃣", 2: "2️⃣", 3: "3️⃣", 4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣", 10: "🔟"}


    class MyModal(discord.ui.Modal):
        def __init__(self, title, embTitle, embNum):
            super().__init__(title=title)
    
            self.add_item(discord.ui.InputText(label="標題", value=embTitle, required=True))
            self.add_item(discord.ui.InputText(label="內容", style=discord.InputTextStyle.long, placeholder="詳細介紹投票內容", required=True))
            self.add_item(discord.ui.InputText(label="選項數量", value=embNum, required=True))
    
        async def callback(self, interaction: discord.Interaction):
            
            def check(ctx, user):
                return user == ctx.message.author 
              
            embed = discord.Embed(title=f"{self.children[0].value}", description=f"{self.children[1].value}")
            
            resp = await interaction.response.send_message(embeds=[embed])    
            request = await resp.original_response()
          
            for emoji in range(int(self.children[2].value)):
                await request.add_reaction(emojis[emoji + 1])
      
            reaction = await Bot.wait_for("reaction_add", check=check)

  
    @Bot.slash_command(name=name, description="建立訊息並偵測反應")
    async def react(ctx, 
                    title: Option(str, "標題", required=True),
                    number: Option(int, "建立選項數量", min_value=1, max_value=10, required=True)
                   ):

        modal = MyModal(title="輸入投票設定", embTitle=title, embNum=number)
        await ctx.send_modal(modal)

        


    @Bot.slash_command(name="1233", description="建立訊息並帶數量貼圖反應")
    async def react(ctx, number: Option(int, "建立數量", min_value=1, max_value=10, required=True)):

        await ctx.respond("建立了一個訊息")
        request = await ctx.send("測試訊息")

        for emoji in range(number):
            await request.add_reaction(emojis[emoji + 1])

    @Bot.command()
    async def hihi(ctx):
        request = await ctx.send("我還在~", stickers=[
          {"name":"👋"}
        ])
        await request.add_reaction("🍦")