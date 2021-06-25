from telethon.errors.rpcerrorlist import YouBlockedUserError
from Extre.utils import extremepro_cmd
import asyncio
    
from pathlib import Path
import asyncio, time, io, math, os, logging, asyncio, shutil, re, subprocess, json
from re import findall
from asyncio import sleep
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from datetime import datetime as dt
from pytz import country_names as c_n, country_timezones as c_tz, timezone as tz
from hachoir.parser import createParser
import pybase64
from base64 import b64decode
from pySmartDL import SmartDL
from telethon.tl.types import DocumentAttributeVideo, DocumentAttributeAudio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url
from html import unescape
from urllib.error import HTTPError
from Extre.utils import extremepro_cmd, edit_or_reply, progress, humanbytes, time_formatter
from Extre import CMD_HELP
import bs4
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL

from youtube_dl.utils import (DownloadError, ContentTooShortError,

                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)

try:

   from youtubesearchpython import SearchVideos 

except:
	os.system("pip install pip install youtube-search-python")
	from youtubesearchpython import SearchVideos 
	pass


@borg.on(extremepro_cmd(pattern="song(?: |$)(.*)"))
async def download_video(v_url):  

    lazy = v_url ; sender = await lazy.get_sender() ; me = await lazy.client.get_me()

    if not sender.id == me.id:
        rkp = await lazy.reply("`processing...`")
    else:
    	rkp = await lazy.edit("`processing...`")   
    url = v_url.pattern_match.group(1)
    if not url:
         return await rkp.edit("`Error \nusage song <song name>`")
    search = SearchVideos(url, offset = 1, mode = "json", max_results = 1)
    test = search.result()
    p = json.loads(test)
    q = p.get('search_result')
    try:
       url = q[0]['link']
    except:
    	return await rkp.edit("`failed to find`")
    type = "audio"
    await rkp.edit("`Preparing to download...`")
    if type == "audio":
        opts = {
            'format':
            'bestaudio',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'writethumbnail':
            True,
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'outtmpl':
            '%(id)s.mp3',
            'quiet':
            True,
            'logtostderr':
            False
        }
        video = False
        song = True    
    try:
        await rkp.edit("`Fetching data, please wait..`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await rkp.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await rkp.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await rkp.edit(
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`"
        )
        return
    except MaxDownloadsReached:
        await rkp.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await rkp.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await rkp.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await rkp.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await rkp.edit("`There was an error during info extraction.`")
        return
    except Exception as e:
        await rkp.edit(f"{str(type(e)): {str(e)}}")
        return
    c_time = time.time()
    if song:
        await rkp.edit(f"`Preparing to upload song:`\
        \n**{rip_data['title']}**\
        \nby *{rip_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(duration=int(rip_data['duration']),
                                       title=str(rip_data['title']),
                                       performer=str(rip_data['uploader']))
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{rip_data['title']}.mp3")))
        os.remove(f"{rip_data['id']}.mp3")
        await v_url.delete()
    elif video:
        await rkp.edit(f"`Preparing to upload song :`\
        \n**{rip_data['title']}**\
        \nby *{rip_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{rip_data['id']}.mp4",
            supports_streaming=True,
            caption=url,
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{rip_data['title']}.mp4")))
        os.remove(f"{rip_data['id']}.mp4")
        await rkp.delete()
        
        
        
import asyncio
import logging
from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot
from userbot.util import admin_cmd, humanbytes

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)


@bot.on(admin_cmd(pattern="music ?(.*)"))  # pylint:disable=E0602
async def music_find(event):
    if event.fwd_from:
        return

    music_name = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if music_name:
        await event.delete()
        song_result = await event.client.inline_query("deezermusicbot", music_name)

        await song_result[0].click(
            event.chat_id,
            reply_to=event.reply_to_msg_id,
            hide_via=True
        )
    elif msg:
        await event.delete()
        song_result = await event.client.inline_query("deezermusicbot", msg.message)

        await song_result[0].click(
            event.chat_id,
            reply_to=event.reply_to_msg_id,
            hide_via=True
        )


@bot.on(admin_cmd(pattern="spotbot ?(.*)"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    msg = await event.get_reply_message()
    await event.delete()

    music_name = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if music_name:
        await event.delete()
        song_result = await event.client.inline_query("spotify_to_mp3_bot", music_name)

        for item_ in song_result:

            if (
                "(FLAC)" in item_.title
                or "(MP3_320)" in item_.title
                or "(MP3_128)" in item_.title
            ):

                j = await item_.click(
                    event.chat_id,
                    reply_to=event.reply_to_msg_id,
                    hide_via=True,
                )

                k = await event.respond(j)
                await j.delete()
                await k.edit("Channel Link:\nhttps://t.me/joinchat/AAAAAE8NqbV48l7ls-pFtQ")

    elif msg:

        await event.delete()
        song_result = await event.client.inline_query("spotify_to_mp3_bot", msg.message)
        for item in song_result:

            if (
                "(FLAC)" in item.title
                or "(MP3_320)" in item.title
                or "(MP3_128)" in item.title
            ):

                j = await item.click(
                    event.chat_id,
                    reply_to=event.reply_to_msg_id,
                    hide_via=True,
                )

                k = await event.respond(j)
                await j.delete()
                await k.edit("Channel Link:\nhttps://t.me/joinchat/AAAAAE8NqbV48l7ls-pFtQ")


@bot.on(admin_cmd(pattern="audioyt ?(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    music_link = event.pattern_match.group(1)
    if music_link:
        chat = "@YTAudioBot"
        async with event.client.conversation(chat) as conv:
            await conv.send_message(music_link)
            await asyncio.sleep(2)
            response = conv.wait_event(events.NewMessage(
                incoming=True, from_users=507379365))
            await event.client.send_message(chat, music_link)
            response = await response
        await event.delete()
        if response.message.media:
            await event.client.send_message(event.chat_id, response)
    else:
        reply_message = await event.get_reply_message()
        chat = "@YTAudioBot"
        sender = reply_message.sender
        await event.edit("```Processing```")
        async with event.client.conversation(chat) as conv:
            response = conv.wait_event(events.NewMessage(
                incoming=True, from_users=507379365))
            await event.client.send_message(chat, reply_message)
            response = await response
            await event.delete()
            if response.message.media:
                await event.client.send_file(event.chat_id, response.message.media)


@bot.on(admin_cmd(pattern="fm ?(.*)"))  # pylint:disable=E0602
async def _(event):
    msg = await event.get_reply_message()
    await event.delete()
    if msg:
        msj = f"[{msg.file.name}](https://t.me/joinchat/AAAAAE8NqbV48l7ls-pFtQ)\n`{humanbytes(msg.file.size)}`"
        await event.client.send_message(
            entity=await event.client.get_entity(-1001326295477),
            file=msg.media,
            message=msj
        )
    else:
        await event.edit("`mesajı yanıtla`")


@bot.on(admin_cmd(pattern="sdown ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("` I need a link to download something pro.`**(._.)**")
    else:
        msg = await event.edit("🎶**Downloading and sending music..!**🎶")
        bot = "@spotify_to_mp3_bot"

        async with event.client.conversation(bot) as conv:
            try:
                await conv.send_message(d_link)
                details = await conv.get_response()
                for row in details.buttons:
                    for button in row:
                        if button.text == "📲🎵Download this Song!":
                            await button.click()
                            first = await conv.get_response()
                            if first.media:
                                msj = f"[{first.media.document.attributes[1].file_name}](https://t.me/joinchat/AAAAAE8NqbV48l7ls-pFtQ)\n`{humanbytes(first.media.document.size)}`"
                                await event.client.send_file(event.chat_id, first, caption=msj)
                                await msg.delete()
                            resp = await conv.get_response()
                            if resp.media:
                                msj = f"[{resp.media.document.attributes[1].file_name}](https://t.me/joinchat/AAAAAE8NqbV48l7ls-pFtQ)\n`{humanbytes(resp.media.document.size)}`"
                                await event.client.send_file(event.chat_id, resp, caption=msj)
                                await msg.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @DeezLoadBot `and retry!`")
            except TimeoutError:
                return
{
        "songs":
        "`.song song name`\
            \nUsage:For searching songs from youtube\
            \n\nsong` Song Title\
            \n\n`.spotbot` Song name\
            \nUsage:Download song from @FindmusicpleaseBot\
            \n\n`.audioyt` Song title\
            \nUsage: song from youtube\
            \n\n`.fm` song name\
            \nUsage:Download song from @DeezLoadBot\
            \n\n`.sdown` <Spotify/Deezer Link>\
            \nUsage:Download music from Spotify or Deezer."
}
