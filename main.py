import BOT
from config import bot 
from pyrogram import idle
import asyncio 
from flask import Flask
from threading import Thread
import random


flask_app = Flask(__name__) 

@flask_app.route('/')
def flask_msg():
  return "TIER BOT RUN"


def run_flask():
  flask_app.run(host="0.0.0.0", port=random.randint(5000, 9999))


def run_thread():
  Thread(target=run_flask).start() 

async def runall():
  run_thread()
  await bot.start()
  idle()
  await bot.stop()



asyncio.run(runall())