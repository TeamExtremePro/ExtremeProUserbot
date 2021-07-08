import heroku3
import re, os
from Extre.variables import Var
from Extre.utils import extremepro_cmd
EXTREMEPRO = Var.HEROKU_APP_NAME
AMANPANDEY = Var.HEROKU_API_KEY
sudolist = os.environ.get("SUDO_USERS", None)
@borg.on(extremepro_cmd(pattern='addsudo'))
async def add_sudo(event):
  Heroku = heroku3.from_key(AMANPANDEY)
  app = Heroku.app(EXTREMEPRO)
  heroku_var = app.config()
  if not event.is_reply:
    return await event.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴘʟᴇᴀsᴇ")                              
  if event.is_reply:
    id = (await event.get_reply_message()).sender_id
    name = (await Andencento.get_entity(id)).first_name
    sudo = heroku_var["SUDO_USERS"]
    op = re.search(str(id), str(sudolist))
    if op:
      await event.edit(f"THE {name} IS ALREADY ON SUDO LIST")
      return
    else:
      pass
    if not sudolist:
       await event.edit(f"𝔒ᴋᴀʏ **{Name}** ɪ𝔰 𝔄ᴅᴅᴇᴅ 𝔒ɴ 𝔰ᴜᴅᴏ ʟɪ𝔰ᴛ (ᴘʟᴇᴀ𝔰ᴇ ᴡᴀɪᴛ ɪ ᴀᴍ ʀᴇ𝔰ᴛᴀʀᴛɪɴɢ)")
       heroku_var["SUDO_USERS"] = id
    else:
       sudousers = f'{sudolist} {id}'
       await event.edit(f"Oᴋᴀʏ **{name}** ɪs ᴀᴅᴅᴇᴅ ᴏɴ sᴜᴅᴏ ᴜsᴇʀs (ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ɪ ᴀᴍ ʀᴇsᴛᴀʀᴛɪɴɢ)")
       heroku_var["SUDO_USERS"] = sudousers
  else:
    await event.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴘʟᴇᴀsᴇ")                              



@borg.on(extremepro_cmd(pattern='rmsudo'))
async def remove_sudo(event):
  Heroku = heroku3.from_key(AMANPANDEY)
  app = Heroku.app(EXTREMEPRO)
  heroku_var = app.config()
  if not event.is_reply:
    return await event.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴘʟᴇᴀsᴇ")
  if event.is_reply:
    id = (await event.get_reply_message()).sender_id
    name = (await Andencento.get_entity(id)).first_name
    op = re.search(str(id), str(sudolist))
    if op:
      i = ""
      amazing = sudolist.split(" ")
      amazing.remove(str(id))
      i += str(amazing)
      x = i.replace("[", "")
      xx = x.replace("]", "")
      xxx = xx.replace(",", "")
      done = xxx.replace("'", "")
      heroku_var["SUDO_USERS"] = done
      await event.edit(f"𝔗ʜᴇ **{name}** ɪ𝔰 ʀᴇᴍᴏᴠᴇᴅ 𝔰ᴜᴄᴄᴇ𝔰𝔰ғᴜʟʟʏ (ᴘʟᴇᴀ𝔰ᴇ ᴡᴀɪᴛ ɪ ᴀᴍ ʀᴇ𝔰ᴛᴀʀᴛɪɴɢ)")
    else:
      await event.edit(f"ᴛʜᴇ {name} ɪ𝔰 ɴᴏᴛ ɪɴ 𝔰ᴜᴅᴏ 😑😑")
    if heroku_var["SUDO_USERS"] == None:
       await event.edit(f"ᴛʜᴇ sᴜᴅᴏ ʟɪsᴛ ɪs ᴇᴍᴘʏᴛʏ 😑😑")
@borg.on(extremepro_cmd("sudo"))
async def sudos(event):
  if sudolist:
    await event.edit("𝔰ᴜᴅᴏ ɪ𝔰 ᴇɴᴇᴀʙʟᴇᴅ")
  else:
     await event.edit("sᴜᴅᴏ ɪs ᴏғғ")            
@borg.on(extremepro_cmd("listsudo"))
async def sudolists(event):
  op = await event.edit('ᴄʜᴇᴄᴋɪɴɢ ᴀʟʟ sᴜᴅᴏs ᴡᴀɪᴛ')
  Heroku = heroku3.from_key(AMANPANDEY)
  app = Heroku.app(EXTREMEPRO)
  heroku_var = app.config()
  if not sudolist:
    return await event.edit("sᴜᴅᴏ ʟɪsᴛ ɪs ᴇᴍᴘᴛʏ")
  sudos = sudolist.split(" ")
  sudoz = "**»sᴜᴅᴏ ʟɪsᴛ«**"
  for sudo in sudos:
    k = await Andencento.get_entity(int(sudo))
    pro = f'\n[**ɴᴀᴍᴇ:** {k.first_name} \n**ᴜsᴇʀɴᴀᴍᴇ:** @{k.chat_id or None}]\n'
    sudoz += pro
  await op.edit(sudoz)
