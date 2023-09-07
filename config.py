from telebot.async_telebot import AsyncTeleBot
import os 

TOKEN = os.environ['TOKEN']
own = [5039288972,1928677026]
ownn = []

bot = AsyncTeleBot(TOKEN, parse_mode='html')