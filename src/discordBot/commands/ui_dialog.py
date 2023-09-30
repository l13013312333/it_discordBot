import discord
from discord.ext import commands

def main(Bot):
    name = "UI-dialog"
    print(f"{name} 註冊成功")


    class DialogModal(discord.ui.Modal):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

            self.add_item(discord.ui.InputText(label="標題"))
            self.add_item(discord.ui.InputText(label="內容", style=discord.InputTextStyle.long))

        async def callback(self, interaction: discord.Interaction):
            embed = discord.Embed(title=self.children[0].value)
            embed.add_field(name="內容", value=self.children[1].value)
            await interaction.response.send_message(embeds=[embed])


    
    @Bot.slash_command(name="敲敲話")
    async def click_click(ctx: discord.ApplicationContext):
        await ctx.send_modal(DialogModal(title="敲敲話"))


    @Bot.command(name="敲敲話")
    async def click_click(ctx: commands.Context):
        class MyView(discord.ui.View):
            @discord.ui.button(label="想要敲敲話", style=discord.ButtonStyle.primary)
            async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
                await interaction.response.send_modal(DialogModal(title="敲敲話"))

        await ctx.send(view=MyView())