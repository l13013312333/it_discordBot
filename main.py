from src.discordBot import DiscordBot
from src.googleSheet import get_sheet

# 測試
# print(get_sheet("測試資料庫")) 

dcBot = DiscordBot()
dcBot.start()
