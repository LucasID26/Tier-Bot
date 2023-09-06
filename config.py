from telebot.async_telebot import AsyncTeleBot
import os 

TOKEN = os.environ['TOKEN']

bot = AsyncTeleBot(TOKEN)