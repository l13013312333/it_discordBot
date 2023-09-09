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
   │  ├─ commandMgr.py # 自動將commands檔案夾註冊，但需要跟著樣版 def main(Bot)
   │  ├─ commands # 需要註冊的內容檔案夾
   │  │  ├─ hello.py # 顯示機器人在不在
   │  │  ├─ messageCommands.py # 訊息指令相關
   │  │  └─ userCommands.py # 玩家指令相關
   │  ├─ eventMgr.py # discord-bot 事件處理 (on_ready、on_message、on_message_edit、on_message_delete)
   │  └─ __init__.py # 建立、初始 discord-bot 
   └─ __init__.py # 初始化用，但為空
```