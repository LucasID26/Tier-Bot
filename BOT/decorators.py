from config import bot,own
from functools import wraps


def admins_only(func):
  @wraps(func)
  async def admins(client, m,*args,**kwargs): 
    if m.from_user.id in own:
      return await func(client, m, *args, **kwargs)
    if m.chat.type == 'private':
      return await func(client, m, *args, **kwargs)
    else:
      admin = await bot.get_chat_members(m.chat.id,m.from_user.id)
      if admin.status.value in ['creator','administrator']:
        return await func(client, m, *args, **kwargs)
      else:
        return await m.reply("Anda harus menjadi admin untuk melakukan ini.")
        
  return admins