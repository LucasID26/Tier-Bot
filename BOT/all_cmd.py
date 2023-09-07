from config import bot 
import json 
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import timezone
from BOT.decorators import admins_only
from pyrogram import filters


get_data = open('BOT/JSON/data.json')
data = json.load(get_data)

async def reset_season():
  global data
  for chatid in data:
    await bot.send_message(int(chatid), "<b>RESET SEASON</b>\nSilahkan push lgi tiermu dengan cara rajin kirim pesan sebanyak mungkin ;)")
    del data[chatid]
  with open('BOT/JSON/data.json','w') as save:
    json.dump(data, save, indent=2)

reset = AsyncIOScheduler(timezone="Asia/Jakarta")
reset.add_job(reset_season, trigger="cron",day=1, hour=0, minute=0)
print("Running PENJADWANLAN SEASON")
reset.start()



@bot.on_message(filters.command(['start','help']))
async def start(client, m):
  global data
  if m.chat.type.value == "private":
    await m.reply(f"Hallo aku adalah {(await bot.get_me()).first_name}\nAku bisa menghitung jumlah pesan yang dikirim oleh user didalam group\nAyo cek Tiermu dengan mengetikan /mytier\n\n-CATATAN: Perintah ini hanya berlaku di group!!")
  else:
    await m.reply("Ayo cek Tiermu dengan mengetikan /mytier")


@bot.on_message(filters.command(['mytier']))
async def tierku(client, m):
  if m.chat.type.value == "private":
    return await m.reply_to("Maaf kamu hanya bisa melihat tiermu didalam group!!")
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
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 31 and point <= 60:
      tier = "Wariorr II"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 61 and point <= 90:
      tier = "Wariorr I"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 91 and point <= 130:
      tier = "Elite III"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 131 and point <= 170:
      tier = "Elite II"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 171 and point <= 210:
      tier = "Elite I"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 211 and point <= 250:
      tier = "Master IV"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 251 and point <= 290:
      tier = "Master IV"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 291 and point <= 330:
      tier = "Master III"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 331 and point <= 370:
      tier = "Master II"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 371 and point <= 410:
      tier = "Master I"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 411 and point <= 450:
      tier = "Grandmaster V"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 451 and point <= 500:
      tier = "Grandmaster IV"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 501 and point <= 550:
      tier = "Grandmaster III"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 551 and point <= 600:
      tier = "Grandmaster II"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 601 and point <= 650:
      tier = "Grandmaster I"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 651 and point <= 700:
      tier = "Epic V"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 701 and point <= 750:
      tier = "Epic IV"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 751 and point <= 800:
      tier = "Epic III"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 801 and point <= 850:
      tier = "Epic II"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 851 and point <= 900:
      tier = "Epic I"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 901 and point <= 950:
      tier = "Legend V"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 951 and point <= 1000:
      tier = "Legend IV"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 1001 and point <= 1050:
      tier = "Legend III"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 1051 and point <= 1100:
      tier = "Legend II"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 1101 and point <= 1150:
      tier = "Legend I"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 1151 and point <= 1250:
      tier = "Mythic Grading"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 1251 and point <= 1400:
      tier = "Mythic"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 1401 and point <= 1750:
      tier = "Mythic Honor"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 1751 and point <= 2150:
      tier = "Mythic Glory"
      await m.reply(msg.format(nama, group, tier, point))
    elif point >= 2151:
      tier = "Mythic Immortal"
      await m.reply(msg.format(nama, group, tier, point))
  else:
    await m.reply("Kamu belum mempunyai Tier!!")


@bot.on_message(filters.command(['grouptier']))
@admins_only
async def groupier(client, m):
  global data
  if m.chat.type.value == "private":
    return await m.reply("Maaf kamu hanya bisa melihat daftar tier didalam group!!")
 
  chatid = str(m.chat.id)
  group = m.chat.title
  if chatid in data:
    user_data = data[chatid]
    sorted_users = sorted(user_data.items(), key=lambda x: x[1]['point'], reverse=True)
    jumlah = 1
    result = f"<b>DAFTAR TIER TETRINGGI</b> {group}\n\n"
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
    await m.reply(result)
  else:
    await m.reply("Belum ada  daftar peringkat!!")







@bot.on_message(filters.text, group=-1)
async def save_point(client, m):
  global data
  if m.chat.type.vlue == "private":
    return
  
  userid = str(m.from_user.id)
  nama = m.from_user.first_name
  chatid = str(m.chat.id)
  if not chatid in data:
    data[chatid] = {}
    with open('BOT/JSON/data.json','w') as save:
      json.dump(data, save, indent=2)
  
  if userid in data[chatid]:
    new_point = 1
    old_point = data[chatid][userid]['point']
    data[chatid][userid]['point'] = old_point + new_point
    with open('BOT/JSON/data.json','w') as save:
      json.dump(data, save, indent=2)

    point = data[chatid][userid]['point']
    msg = """SELAMAT {}

Kamu mengalami kenaikan TIER
<b>TIER:</b> {}
<b>POINT:</b> {}
"""
    if point == 31:
      tier = "Wariorr II"
      await m.reply(msg.format(nama, tier, point))
    elif point == 61:
      tier = "Wariorr I"
      await m.reply(msg.format(nama, tier, point))
    elif point == 91:
      tier = "Elite III"
      await m.reply(msg.format(nama, tier, point))
    elif point == 131:
      tier = "Elite II"
      await m.reply(msg.format(nama, tier, point))
    elif point == 171:
      tier = "Elite I"
      await m.reply(msg.format(nama, tier, point))
    elif point == 211:
      tier = "Master IV"
      await m.reply(msg.format(nama, tier, point))
    elif point == 251:
      tier = "Master IV"
      await m.reply(msg.format(nama, tier, point))
    elif point == 291:
      tier = "Master III"
      await m.reply(msg.format(nama, tier, point))
    elif point == 331:
      tier = "Master II"
      await m.reply(msg.format(nama, tier, point))
    elif point == 371:
      tier = "Master I"
      await m.reply(msg.format(nama, tier, point))
    elif point == 411:
      tier = "Grandmaster V"
      await m.reply(msg.format(nama, tier, point))
    elif point == 451:
      tier = "Grandmaster IV"
      await m.reply(msg.format(nama, tier, point))
    elif point == 501:
      tier = "Grandmaster III"
      await m.reply(msg.format(nama, tier, point))
    elif point == 551:
      tier = "Grandmaster II"
      await m.reply(msg.format(nama, tier, point))
    elif point == 601:
      tier = "Grandmaster I"
      await m.reply(msg.format(nama, tier, point))
    elif point == 651:
      tier = "Epic V"
      await m.reply(msg.format(nama, tier, point))
    elif point == 701:
      tier = "Epic IV"
      await m.reply(msg.format(nama, tier, point))
    elif point == 751:
      tier = "Epic III"
      await m.reply(msg.format(nama, tier, point))
    elif point == 801:
      tier = "Epic II"
      await m.reply(msg.format(nama, tier, point))
    elif point == 851:
      tier = "Epic I"
      await m.reply(msg.format(nama, tier, point))
    elif point == 901:
      tier = "Legend V"
      await m.reply(msg.format(nama, tier, point))
    elif point == 951:
      tier = "Legend IV"
      await m.reply(msg.format(nama, tier, point))
    elif point == 1001:
      tier = "Legend III"
      await m.reply(msg.format(nama, tier, point))
    elif point == 1051:
      tier = "Legend II"
      await m.reply(msg.format(nama, tier, point))
    elif point == 1101:
      tier = "Legend I"
      await m.reply(msg.format(nama, tier, point))
    elif point == 1151:
      tier = "Mythic Grading"
      await m.reply(msg.format(nama, tier, point))
    elif point == 1251:
      tier = "Mythic"
      await m.reply(msg.format(nama, tier, point))
    elif point == 1401:
      tier = "Mythic Honor"
      await m.reply(msg.format(nama, tier, point))
    elif point == 1751:
      tier = "Mythic Glory"
      await m.reply(msg.format(nama, tier, point))
    elif point == 2151:
      tier = "Mythic Immortal"
      await m.reply(msg.format(nama, tier, point))

  else:
    point = 1
    data[chatid][userid] = {"nama": nama, "point": point}
    with open('BOT/JSON/data.json','w') as save:
      json.dump(data, save, indent=2)







