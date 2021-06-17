#MADE BY @GODBOYX AND @AmanPandeyDeveloperIN
#MADE FOR Extre USERBOT ONLY
#KANG WITH CREDITS OTHERWISE YOU WILL See What We can Do 
from Extre.utils import admin_cmd
from .. import CMD_HELP
import os
from PIL import Image, ImageDraw, ImageFont

@borg.on(admin_cmd(pattern="^/logo ?(.*)"))
async def logo(event):
 await event.reply('Drawing Text On Pic.Wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./Extre/resources/photo_2021-03-18_10-37-51.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "red"
    shadowcolor = "blue"
    font = ImageFont.truetype("./Extre/resources/Vampire_Wars.otf", 160)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=15, stroke_fill="yellow")
    fname2 = "LogoByDynamic.png"
    img.save(fname2, "png")
    await bot.send_file(event.chat_id, fname2, caption="Made By Extre")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @ExtreUSERBOTSUPPORT {e}')

file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 In Beta!.
 - .logo <text>

"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
