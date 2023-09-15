import discord

def main(Bot):
    name = "UI-select"
    print(f"{name} 註冊成功")

    class SelectView(discord.ui.View):
        def __init__(self, author, timeout=180):
            super().__init__(timeout=timeout)
            self.author = author

        async def interaction_check(self, interaction: discord.Interaction):
            return interaction.user.id == self.author.id

        @discord.ui.select(placeholder = "選擇", min_values=1, max_values=1, options=[
            discord.SelectOption(label="A", description="讓他告訴你未來一年間發生的事"),
            discord.SelectOption(label="B", description="讓他告訴你明天發生的事"),
            discord.SelectOption(label="C", description="讓他什麼都不要說"),
        ]
        )
        async def select_callback(self, select:discord.ui.Select, interaction:discord.Interaction):
            select.disabled = True
            msg = None
            if select.values[0] is "A": msg = "你的外表看起來隨和、好相處，但內裡其實有點固執，意志非常的堅強，面對自己在乎的事情會非常執著。"
            elif select.values[0] is "B": msg = "你的個性有點急躁，想到什麼就做什麼，但也非常的單純，從來不記仇，社交能力很強，是大家的開心果。"
            else : msg = "你總是非常的小心謹慎，個性有點內向，不太懂得如何表達自己的情感面，很多時候你更喜歡自己待著，會讓你感到相較自在。"
            await interaction.response.edit_message(content=msg ,view=None)


    
    @Bot.command(name="選單")
    async def click_click(ctx):
        await ctx.send('路上有個老人擁有預知能力，並可以告知你一些事情，你希望...', view=SelectView(ctx.author))
