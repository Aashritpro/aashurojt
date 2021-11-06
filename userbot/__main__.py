from userbot import bot
from sys import argv
import sys
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from userbot.utils import load_module, start_assistant, load_addons, load_abuse, start_spam
from userbot.utils import *
from userbot import LOAD_PLUG, LOGS, LEGENDversion
from pathlib import Path
import asyncio
import glob
import telethon.utils

l2= Config.SUDO_COMMAND_HAND_LER
LEGEND_PIC = "https://telegra.ph/file/e753315316673cff51085.mp4"
l1 = Config.COMMAND_HAND_LER



async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        print(f"LEGEND_STRING - {str(e)}")
        sys.exit()
        
        
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Var.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
            ).start(bot_token=Var.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("♥️ Starting LegendBot ♥️")
            bot.loop.run_until_complete(add_bot(Config.BOT_USERNAME))
            LOGS.info("🥇🔥 LegendBot Startup Completed 🔥🥇")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

print("📍⚜Loading Modules / Plugins⚜✔")


async def module():
  import glob
  path = 'userbot/plugins/*.py'
  files = glob.glob(path)
  for name in files:
    with open(name) as f:
      path1 = Path(f.name)
      shortname = path1.stem
      load_module(shortname.replace(".py", ""))
    
assistant = os.environ.get("ASSISTANT", None)
async def assistants():
    if assistant == "ON":
        import glob
        path = 'userbot/plugins/assistant/*.py'
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                try:
                    start_assistant(shortname.replace(".py", ""))   
                except Exception as e:
                    print(e)
    else:
        print("⚠️Assistant Not Loaded⚠️")

addon = os.environ.get("EXTRA_PLUGIN", None)             
async def addons():
    if addon == "ON":
        import glob
        path = 'userbot/plugins/Xtra_Plugin/*.py'
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                try:
                    load_addons(shortname.replace(".py", ""))
                except Exception as e:
                    print(e)
    else:
        print("⚠️Addons Not Loading⚠️")
       


abuse = os.environ.get("ABUSE", None) 
async def abuses():
    if abuse == "ON":
        import glob
        path = 'userbot/plugins/Abuse/*.py'
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                try:
                    load_abuse(shortname.replace(".py", ""))    
                except Exception as e:
                    print(e)     
    else:
        print("⚠️Abuse Not Loading⚠️")

spam = os.environ.get("SPAM", None)
async def spams():
    if spam == "ON":
        import glob
        path = 'userbot/plugins/Spam/*.py'
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                try:
                    start_spam(shortname.replace(".py", ""))  
                except Exception as e:
                    print(e)       
    else:
        print("⚠️Spam Not Loading⚠️")

bot.loop.run_until_complete(module())
bot.loop.run_until_complete(addons())
bot.loop.run_until_complete(abuses())
bot.loop.run_until_complete(assistants())
bot.loop.run_until_complete(spams())

print(f"""♥️🇮🇳♥️⚜♥️
╔════❰LEGENDBOT❱═❍⊱❁۪۪
║┣⪼ OWNER - LEGEND
║┣⪼ Group - @Legend_Userbot
║┣⪼ CREATOR - @The_LegendBoy
║┣⪼ TELETHON - 1.2.0
║┣⪼ ✨ 『🔱🇱 🇪 🇬 🇪 🇳 🇩 🔱』𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱""")

async def legend_op():
    try:
        os.environ["LEGEND_STRING"] = "Protected By LegendBot"
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                LEGEND_PIC,
                caption=f"#START \nDeployed LEGENDBOT Successfully\n\n**LEGENDBOT- {LEGENDversion}**\n\nType `{l1}help` or `{l1}ping` to check! \n\nJoin [LegendBot Channel](t.me/Official_LegendBot) for Updates & [LegendBot Chat](t.me/Legend_Userbot) for any query regarding LegendBot",
            )
    except Exception as e:
        print(str(e))

# Join LegndBot Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@Official_LegendBot"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@Legend_Userbot"))
    except BaseException:
         pass

bot.loop.create_task(legend_op())
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()
