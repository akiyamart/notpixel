from dotenv import load_dotenv
import os 
from envparse import Env
from aiogram import Bot, Dispatcher

env = Env()
load_dotenv()

class ConfigBot:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Bot(token=ConfigBot.BOT_TOKEN)
dp = Dispatcher()