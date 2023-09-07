from config import bot,own
from functools import wraps

def bot_admin(func):
  @wraps(func)
  async def admins(m,*args,**kwargs):
    imbot = await bot.get_me()
    idbot = imbot.id
    if m.from_user.id in own:
      return await func(m,*args,**kwargs)
    if m.chat.type == 'private':
      return await func(m,*args,**kwargs) 
    else:
      infobot = await bot.get_chat_member(m.chat.id,idbot)
      if infobot.status in ['creator','administrator']:
        return await func(m,*args,**kwargs)
      else:
        return await bot.reply_to(m, "Saya harus menjadi admin untuk menjalankan perintah ini.")
  return admins



def admins_only(func):
  @wraps(func)
  async def admins(m,*args,**kwargs): 
    if m.from_user.id in own:
      return await func(m, *args, **kwargs)
    if m.chat.type == 'private':
      return await func(m, *args, **kwargs)
    else:
      admin = await bot.get_chat_member(m.chat.id,m.from_user.id)
      if admin.status in ['creator','administrator']:
        return await func(m, *args, **kwargs)
      else:
        return await bot.reply_to(m, "Anda harus menjadi admin untuk melakukan ini.")
  return admins