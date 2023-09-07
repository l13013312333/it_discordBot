import os
import importlib

def _init(Bot):
	print(Bot)
	path = os.path.join(os.getcwd() + "/src/discordBot/commands")
	dirs = os.listdir(path)

	for file in dirs:
		if (file.endswith(".py")): 
			fileName = file.replace(".py", "")
			module  = importlib.import_module("src.discordBot.commands."+fileName)
			module.main(Bot)