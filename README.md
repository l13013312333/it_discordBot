# IT Discord.py bot
為參加IT鐵人賽 而做的示範CODE

## 套件
```
discord --version // 3.x 以上
pip install py-cord
pip install discord.py
```

## 目錄結構
```
it_discordBot
├─ main.py # 程式進入點
└─ src # 包裝
   ├─ discordBot # discrod-bot內容
   │  ├─ commandMgr.py     # 自動將commands檔案夾註冊，但需要跟著樣版 def main(Bot)
   │  ├─ commands          # 註冊命令資料夾
   │  ├─ schedule          # 註冊排程
   │  ├─ eventMgr.py       # discord-bot 事件處理 (on_ready、on_message、on_message_edit、on_message_delete)
   │  └─ __init__.py       # 建立、初始 discord-bot 
   │
   ├── __init__.py         # 初始化用，但為空
   ├── googleAppSheet.py   # Google AppSheet API
   └── googleSheet.py      # Google Sheet API
```

## .env 該填入值
參數| 說明
----|------
DISCORD_TOKEN | 機器人Token
GOOGLE_SHEET_ID | 連接的 google 試算表ID
GOOGLE_APPSHEET_TOKEN | 連接 google app sheet Token
GOOGLE_APPSHEET_ID | google app sheet ID
SECRET_KEY | GOOGLE Youtube API 用KEY