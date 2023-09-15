import discord

def main(Bot):
    name = "UI-button"
    print(f"{name} 註冊成功")

    class ButtonView(discord.ui.View):
        def __init__(self, author, timeout=180):
            super().__init__(timeout=timeout)
            self.author = author

        async def interaction_check(self, interaction: discord.Interaction):
            return interaction.user.id == self.author.id
            #await interaction.response.send_message("收到你的點擊")
            
        @discord.ui.button(label="點擊", style=discord.ButtonStyle.primary)
        async def button_callback(self, button:discord.ui.Button, interaction:discord.Interaction):
            button.disabled = True
            await interaction.response.edit_message(view=self)
            #await interaction.response.send_message("收到你的點擊")


    
    @Bot.command(name="按鈕產生器")
    async def click_click(ctx):
        await ctx.send('生出了一個按鈕', view=ButtonView(ctx.author))
