""" Userbot module for frying stuff. ported by @ExtremeProUserbot """
import io
from random import randint, uniform

from PIL import Image, ImageEnhance, ImageOps
from telethon.tl.types import DocumentAttributeFilename
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="deepfry(?: |$)(.*)", outgoing=True))
async def deepfryer(event):
    try:
        frycount = int(event.pattern_match.group(1))
        if frycount < 1:
            raise ValueError
    except ValueError:
        frycount = 1
    if event.is_reply:
        reply_message = await event.get_reply_message()
        data = await check_media(reply_message)
        if isinstance(data, bool):
            await event.edit("`I can't deep fry that!`")
            return
    else:
        await event.edit("`Reply to an image or sticker to deep fry it!`")
        return
    await event.edit("`Downloading media…`")
    image = io.BytesIO()
    await event.client.download_media(data, image)
    image = Image.open(image)
    await event.edit("`Deep frying media…`")
    for _ in range(frycount):
        image = await deepfry(image)
    fried_io = io.BytesIO()
    fried_io.name = "image.jpeg"
    image.save(fried_io, "JPEG")
    fried_io.seek(0)
    await event.reply(file=fried_io)


async def deepfry(img: Image) -> Image:
    colours = (
        (randint(50, 200), randint(40, 170), randint(40, 190)),
        (randint(190, 255), randint(170, 240), randint(180, 250)),
    )
    img = img.copy().convert("RGB")
    img = img.convert("RGB")
    width, height = img.width, img.height
    img = img.resize(
        (int(width ** uniform(0.8, 0.9)), int(height ** uniform(0.8, 0.9))),
        resample=Image.LANCZOS,
    )
    img = img.resize(
        (int(width ** uniform(0.85, 0.95)), int(height ** uniform(0.85, 0.95))),
        resample=Image.BILINEAR,
    )
    img = img.resize(
        (int(width ** uniform(0.89, 0.98)), int(height ** uniform(0.89, 0.98))),
        resample=Image.BICUBIC,
    )
    img = img.resize((width, height), resample=Image.BICUBIC)
    img = ImageOps.posterize(img, randint(3, 7))
    overlay = img.split()[0]
    overlay = ImageEnhance.Contrast(overlay).enhance(uniform(1.0, 2.0))
    overlay = ImageEnhance.Brightness(overlay).enhance(uniform(1.0, 2.0))
    overlay = ImageOps.colorize(overlay, colours[0], colours[1])
    img = Image.blend(img, overlay, uniform(0.1, 0.4))
    img = ImageEnhance.Sharpness(img).enhance(randint(5, 300))
    return img


async def check_media(reply_message):
    if reply_message and reply_message.media:
        if reply_message.photo:
            data = reply_message.photo
        elif reply_message.document:
            if (
                DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
                in reply_message.media.document.attributes
            ):
                return False
            if (
                reply_message.gif
                or reply_message.video
                or reply_message.audio
                or reply_message.voice
            ):
                return False
            data = reply_message.media.document
        else:
            return False
    else:
        return False
    if not data or data is None:
        return False
    else:
        return data
