from config import bot,own
import json 
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import timezone
from BOT.decorators import admins_only,bot_admin


file = 'BOT/JSON/data.json'
backup = 'BOT/JSON/backup.json'

async def reset_season():
  data = json.load(open(file))
  for chatid in data:
    await bot.send_message(int(chatid), "<b>RESET SEASON</b>\nSilahkan push lgi tiermu dengan cara rajin kirim pesan sebanyak mungkin ;)")
    del data[chatid]
  await save(data)

reset = AsyncIOScheduler(timezone="Asia/Jakarta")
reset.add_job(reset_season, trigger="cron",minute=0, hour=0, day=1)
print("Running PENJADWANLAN SEASON")
reset.start()
jobs = reset.get_jobs()
for job in jobs:
    print(job)

async def save(data):
  with open(file,'w') as save:
    json.dump(data, save, indent=2)





@bot.message_handler(commands=['start','help'])
async def start(m):
  data = json.load(open(file))
  if m.chat.type == "private":
    jumlah = 0
    for i in data:
      jumlah += 1
    await bot.reply_to(m, f"Hallo aku adalah {(await bot.get_me()).first_name}\nAku bisa menghitung jumlah pesan yang dikirim oleh user didalam group\nAyo cek Tiermu dengan mengetikan /mytier\n\n-CATATAN: Perintah ini hanya berlaku di group!!\n<b>Dipakai:</b> {jumlah} Group")
  else:
    await bot.reply_to(m, "Ayo cek Tiermu dengan mengetikan /mytier")


@bot.message_handler(commands=['mytier'])
async def tierku(m):
  data = json.load(open(file))
  if m.chat.type == "private":
    return await bot.reply_to(m, "Maaf kamu hanya bisa melihat tiermu didalam group!!")
  userid = str(m.from_user.id)
  chatid = str(m.chat.id)
  group = m.chat.title
  msg = """Halo ‎{} ️,
  
Tier kamu di group {} saat ini adalah <b>[ {} ]</b> dengan total rutinitas terkirim pesan di grup sebanyak : <b>{}</b> Pesan.

Ayo tingkatkan aktifitas kamu di grup dengan mengirimkan pesan yang bermanfaat atau sekedar ingin chit-chat gabutan
"""
  if userid in data[chatid]:
    nama = data[chatid][userid]['nama']
    point = data[chatid][userid]['point']
    if point >= 0 and point <= 30:
      tier = "Wariorr III"
    elif point >= 0 and point <= 30:
      tier = "Wariorr III"
    elif point >= 31 and point <= 60:
      tier = "Wariorr II"
    elif point >= 61 and point <= 90:
      tier = "Wariorr I"
    elif point >= 91 and point <= 130:
      tier = "Elite III"
    elif point >= 131 and point <= 170:
      tier = "Elite II"
    elif point >= 171 and point <= 210:
      tier = "Elite I"
    elif point >= 211 and point <= 250:
      tier = "Master IV"
    elif point >= 251 and point <= 290:
      tier = "Master IV"
    elif point >= 291 and point <= 330:
      tier = "Master III"
    elif point >= 331 and point <= 370:
      tier = "Master II"
    elif point >= 371 and point <= 410:
      tier = "Master I"
    elif point >= 411 and point <= 450:
      tier = "Grandmaster V"
    elif point >= 451 and point <= 500:
      tier = "Grandmaster IV"
    elif point >= 501 and point <= 550:
      tier = "Grandmaster III"
    elif point >= 551 and point <= 600:
      tier = "Grandmaster II"
    elif point >= 601 and point <= 650:
      tier = "Grandmaster I" 
    elif point >= 651 and point <= 700:
      tier = "Epic V"  
    elif point >= 701 and point <= 750:
      tier = "Epic IV"
    elif point >= 751 and point <= 800:
      tier = "Epic III"
    elif point >= 801 and point <= 850:
      tier = "Epic II"
    elif point >= 851 and point <= 900:
      tier = "Epic I"
    elif point >= 901 and point <= 950:
      tier = "Legend V"
    elif point >= 951 and point <= 1000:
      tier = "Legend IV"
    elif point >= 1001 and point <= 1050:
      tier = "Legend III"
    elif point >= 1051 and point <= 1100:
      tier = "Legend II"
    elif point >= 1101 and point <= 1150:
      tier = "Legend I"
    elif point >= 1151 and point <= 1250:
      tier = "Mythic Grading"
    elif point >= 1251 and point <= 1400:
      tier = "Mythic"
    elif point >= 1401 and point <= 1750:
      tier = "Mythic Honor"
    elif point >= 1751 and point <= 2150:
      tier = "Mythic Glory"
    elif point >= 2151:
      tier = "Mythic Immortal"
    await bot.reply_to(m, msg.format(nama, group, tier, point))
  else:
    await bot.reply_to(m, "Kamu belum mempunyai Tier!!")


@bot.message_handler(commands=['grouptier'])
@bot_admin
@admins_only
async def groupier(m):
  data = json.load(open(file))
  if m.chat.type == "private":
    return await bot.reply_to(m, "Maaf kamu hanya bisa melihat daftar tier didalam group!!")
 
  chatid = str(m.chat.id)
  group = m.chat.title
  if chatid in data:
    user_data = data[chatid]
    sorted_users = sorted(user_data.items(), key=lambda x: x[1]['point'], reverse=True)
    jumlah = 1
    result = f"<b>DAFTAR TIER TERTINGGI</b> {group}\n\n"
    for i, (userid, userdata) in enumerate(sorted_users[:10]):
      nama = userdata['nama']
      point = userdata['point']
      if point >= 0 and point <= 30:
        tier = "Wariorr III"
      elif point >= 31 and point <= 60:
        tier = "Wariorr II"
      elif point >= 61 and point <= 90:
        tier = "Wariorr I"
      elif point >= 91 and point <= 130:
        tier = "Elite III"
      elif point >= 131 and point <= 170:
        tier = "Elite II"
      elif point >= 171 and point <= 210:
        tier = "Elite I"
      elif point >= 211 and point <= 250:
        tier = "Master IV"
      elif point >= 251 and point <= 290:
        tier = "Master IV"
      elif point >= 291 and point <= 330:
        tier = "Master III"
      elif point >= 331 and point <= 370:
        tier = "Master II"
      elif point >= 371 and point <= 410:
        tier = "Master I"
      elif point >= 411 and point <= 450:
        tier = "Grandmaster V"
      elif point >= 451 and point <= 500:
        tier = "Grandmaster IV"
      elif point >= 501 and point <= 550:
        tier = "Grandmaster III"
      elif point >= 551 and point <= 600:
        tier = "Grandmaster II"
      elif point >= 601 and point <= 650:
        tier = "Grandmaster I" 
      elif point >= 651 and point <= 700:
        tier = "Epic V"  
      elif point >= 701 and point <= 750:
        tier = "Epic IV"
      elif point >= 751 and point <= 800:
        tier = "Epic III"
      elif point >= 801 and point <= 850:
        tier = "Epic II"
      elif point >= 851 and point <= 900:
        tier = "Epic I"
      elif point >= 901 and point <= 950:
        tier = "Legend V"
      elif point >= 951 and point <= 1000:
        tier = "Legend IV"
      elif point >= 1001 and point <= 1050:
        tier = "Legend III"
      elif point >= 1051 and point <= 1100:
        tier = "Legend II"
      elif point >= 1101 and point <= 1150:
        tier = "Legend I"
      elif point >= 1151 and point <= 1250:
        tier = "Mythic Grading"
      elif point >= 1251 and point <= 1400:
        tier = "Mythic"
      elif point >= 1401 and point <= 1750:
        tier = "Mythic Honor"
      elif point >= 1751 and point <= 2150:
        tier = "Mythic Glory"
      elif point >= 2151:
        tier = "Mythic Immortal"

      result += f"{jumlah}.{nama} => {point} [ {tier} ]\n"
      jumlah += 1
    await bot.reply_to(m, result)
  else:
    await bot.reply_to(m, "Belum ada  daftar peringkat!!")


@bot.message_handler(commands=['backup'])
async def backup_data(m):
  if m.from_user.id in own:
    with open(file, 'r') as sumber_file:
      data_sumber = json.load(sumber_file)
    with open(backup, 'w') as tujuan_file:
      json.dump(data_sumber, tujuan_file, indent=2)
    await bot.reply_to(m, f"<code>Data dari file sumber telah disalin ke file backup.</code>")
  else:
    return




@bot.message_handler(func=lambda message: True)
async def save_point(m):
  data = json.load(open(file))
  if m.chat.type == "private":
    return
  
  userid = str(m.from_user.id)
  nama = m.from_user.first_name
  chatid = str(m.chat.id)
  if not chatid in data:
    data[chatid] = {}
    await save(data)
  
  if userid in data[chatid]:
    new_point = 1
    old_point = data[chatid][userid]['point']
    data[chatid][userid]['point'] = old_point + new_point
    await save(data)

    point = data[chatid][userid]['point']
    msg = """SELAMAT {}

Kamu mengalami kenaikan TIER
<b>TIER:</b> {}
<b>POINT:</b> {}
"""
    if point == 31:
      tier = "Wariorr II"
    elif point == 61:
      tier = "Wariorr I"
    elif point == 91:
      tier = "Elite III"
    elif point == 131:
      tier = "Elite II"
    elif point == 171:
      tier = "Elite I"
    elif point == 211:
      tier = "Master IV"
    elif point == 251:
      tier = "Master IV"
    elif point == 291:
      tier = "Master III"
    elif point == 331:
      tier = "Master II"
    elif point == 371:
      tier = "Master I"
    elif point == 411:
      tier = "Grandmaster V"
    elif point == 451:
      tier = "Grandmaster IV"
    elif point == 501:
      tier = "Grandmaster III"
    elif point == 551:
      tier = "Grandmaster II"
    elif point == 601:
      tier = "Grandmaster I"
    elif point == 651:
      tier = "Epic V"
    elif point == 701:
      tier = "Epic IV"
    elif point == 751:
      tier = "Epic III"
    elif point == 801:
      tier = "Epic II"
    elif point == 851:
      tier = "Epic I"
    elif point == 901:
      tier = "Legend V"
    elif point == 951:
      tier = "Legend IV"
    elif point == 1001:
      tier = "Legend III"
    elif point == 1051:
      tier = "Legend II"
    elif point == 1101:
      tier = "Legend I"
    elif point == 1151:
      tier = "Mythic Grading"
    elif point == 1251:
      tier = "Mythic"
    elif point == 1401:
      tier = "Mythic Honor"
    elif point == 1751:
      tier = "Mythic Glory"
    elif point == 2151:
      tier = "Mythic Immortal"
    else:
      return
    await bot.reply_to(m, msg.format(nama, tier, point))

  else:
    point = 1
    data[chatid][userid] = {"nama": nama, "point": point}
    await save(data)




