from config import bot 
import json 

@bot.message_hanler(commands=['start','help'])
async def start(m):
  await bot.reply_to(m, "Hallo")

get_data = open('JSON/data.json')
data = json.load(get_data)
@bot.messagw_handler(commands=['mytier'])
async def tierku(m):
  userd = m.from_user.id
  if userid in data:
    nama = data[userid]['nama']
    point = data[userid]['point']
    if point >= 0 and point <= 39:
      await bot.reply_to(m, "Kamu newbie")