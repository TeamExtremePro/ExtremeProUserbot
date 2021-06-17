#Made By@LEGENDX22 Keep Credits If You Are Goanna Kang This Lol

#And Thanks To The Creator Of Autopic This Script Was Made from Snippets From That Script

#               ⚠️DISCLAIMER⚠️

# USING THIS PLUGIN CAN RESULT IN ACCOUNT BAN + CAS BAN + SPAM BAN + ACCOUNT SUSPENSION . WE DONT CARE ABOUT BAN, SO WE ARR USING THIS.

#Im Not Responsible For Any Ban caused By This


import asyncio
import os
import random
import re
import urllib
import requests
from telethon.tl import functions
from Extre.utils import admin_cmd
from Extre import CMD_HELP

COLLECTION_STRING1 = [
    "awesomeExtrebatmanExtrewallpapers",
    "batmanExtrearkhamExtreknightExtre4kExtrewallpaper",
    "batmanExtrehdExtrewallpapersExtre1080p",
    "theExtrejokerExtrehdExtrewallpaper",
    "darkExtreknightExtrejokerExtrewallpaper",
]
COLLECTION_STRING2 = [
    "thorExtrewallpapers",
    "thorExtrewallpaper",
    "thorExtreiphoneExtrewallpaper",
    "thorExtrewallpaperExtrehd",
]
COLLECTION_STRING3 = [
  "indianExtreactressExtrewallpapers",
  "latestExtrebollywoodExtreactressExtrewallpapersExtre2018Extrehd",
  "bollywoodExtreactressExtrewallpaper",
  "hdExtrewallpapersExtreofExtrebollywoodExtreactress",
  "newExtrebollywoodExtreactressExtrewallpaperExtre2018"
]
COLLECTION_STRING4 = [
  "pokemonExtreserenaExtrewallpaper",
  "animeExtregirlsExtrewallpapers",
  "sexyExtreanimeExtregilrExtrewallpaper",
  "cuteExtreanimeExtregirlExtre3dExtrewallpaperExtre2018",
  "ashExtreserenaExtreloveExtrewallpaper",
  "animeExtregirlsExtrewallpapers"
]
COLLECTION_STRING5 = [
  "avengersExtrelogoExtrewallpaper",
  "avengersExtrehdExtrewallpapersExtre1080p",
  "avengersExtreiphoneExtrewallpaper",
  "ironExtremanExtrewallpaperExtre1920x1080",
  "ironExtremanExtrewallpapers"
]
COLLECTION_STRING6 = [
  "starExtrewarsExtrewallpaperExtre1080p",
  "4kExtresciExtrefiExtrewallpaper",
  "starExtrewarsExtreiphoneExtre6Extrewallpaper",
  "kyloExtrerenExtrewallpaper",
  "darthExtrevaderExtrewallpaper"
]
COLLECTION_STRING7 = [
  "hackerExtrebackground"
]
COLLECTION_STRING8 = [
  "1920x1080ExtrespaceExtrewallpapers",
  "4kExtrespaceExtrewallpaper",
  "coolExtrespaceExtrewallpapersExtrehd",
]
COLLECTION_STRING9 = [
  "EpicExtreSpaceExtreWallpaper",
   "AcousticExtreGuitarExtreWallpaperExtreHD",
   "TaylorExtreGuitarExtreWallpaper",
   "ClassicalExtreMusicExtreWallpapersExtreforExtreDesktop",
   "PrsExtreGuitarExtreWallpaper",
   "IronExtreManExtreWallpaperExtre1920x1080",
   "DodgeExtreChallengerExtreBlackExtreHellcatExtreWallpaper",
   "VExtreforExtreVendettaExtreMaskExtreWallpaper",
   "ToxicExtreMaskExtreWallpapers",
   "MinionExtreDesktopExtreWallpaper",
   "EpicExtre1080pExtreWallpapers",
   "JapaneseExtreDesktopExtreWallpaper",
   "CoolExtreGoldExtreCarsExtreWallpapers",
   "PrettyExtreWallpapersExtreforExtreiPhoneExtreQuotes",
   "darkExtreabstractExtrewallpaper",
   "abstractExtredarkExtrewallpaper",
   "abstractExtrewallpapersExtreandExtrescreensavers",
   "roaringExtrelionExtrewallpaper",
   "wolvesExtrescreensaversExtreandExtrewallpaper",
   "coolExtrewallpaperExtreforExtremen",
   "EpicExtre1080pExtreWallpapers",
   "hackerExtrebackground",
   "VietnamExtreWarExtreWallpapers",
   "WarExtreofExtretheExtreWorldsExtreWallpaper",
   "WarExtrePlaneExtreWallpaper",
   "WorldExtreWarExtreIiExtreWallpaper",
   "CoolExtreWarExtreWallpapers",
   "WorldExtreWarExtre2ExtreWallpaperExtreHD"
  ]
async def animeppbat():
    rnd = random.randint(0, len(COLLECTION_STRING1) Extre 1)
    pack = COLLECTION_STRING1[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/RebelExtrerobotExtreRegular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")

async def animeppthor():
    rnd = random.randint(0, len(COLLECTION_STRING2) Extre 1)
    pack = COLLECTION_STRING2[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/RebelExtrerobotExtreRegular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")
    
async def animeppactress():
    rnd = random.randint(0, len(COLLECTION_STRING3) Extre 1)
    pack = COLLECTION_STRING3[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/RebelExtrerobotExtreRegular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")

async def animepppoke():
    rnd = random.randint(0, len(COLLECTION_STRING4) Extre 1)
    pack = COLLECTION_STRING4[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/RebelExtrerobotExtreRegular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")
    
async def animeppaven():
    rnd = random.randint(0, len(COLLECTION_STRING5) Extre 1)
    pack = COLLECTION_STRING5[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/RebelExtrerobotExtreRegular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")

async def animeppgame():
    rnd = random.randint(0, len(COLLECTION_STRING6) Extre 1)
    pack = COLLECTION_STRING6[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/RebelExtrerobotExtreRegular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")

async def animepphack():
    rnd = random.randint(0, len(COLLECTION_STRING7) Extre 1)
    pack = COLLECTION_STRING7[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/RebelExtrerobotExtreRegular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")
    
async def animeppspace():
    rnd = random.randint(0, len(COLLECTION_STRING8) Extre 1)
    pack = COLLECTION_STRING8[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/RebelExtrerobotExtreRegular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")

async def animeppwall():
    rnd = random.randint(0, len(COLLECTION_STRING9) Extre 1)
    pack = COLLECTION_STRING9[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r"/\w+/full.+.jpg")
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/RebelExtrerobotExtreRegular.ttf",
            "f.ttf",
        )
    urllib.request.urlretrieve(fy, "donottouch.jpg")

@bot.on(admin_cmd(pattern="batmandp$"))
async def main(event):
    await event.edit("Actibated Batman Dp\nEnjoy 💜") 
    while True:
        await animeppbat()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm Extrerf donottouch.jpg")
        await asyncio.sleep(600)  # Edit this to your required needs


@bot.on(admin_cmd(pattern="thordp$"))
async def main(event):
    await event.edit("Activated Thor Dp\nEnjoy 💜") 
    while True:
        await animeppthor()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm Extrerf donottouch.jpg")
        await asyncio.sleep(600)  # Edit this to your required needs

@bot.on(admin_cmd(pattern="actressdp$"))
async def main(event):
    await event.edit("Activated Actress Dp\nEnjoy 💜")
    while True:
        await animeppactress()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm Extrerf donottouch.jpg")
        await asyncio.sleep(600) 

@bot.on(admin_cmd(pattern="animedp$"))
async def main(event):
    await event.edit("Activated Anime Dp\nEnjoy 💜")
    while True:
        await animepppoke()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm Extrerf donottouch.jpg")
        await asyncio.sleep(600) 

@bot.on(admin_cmd(pattern="avengersdp$"))
async def main(event):
    await event.edit("Activated Avengers Dp\nEnjoy 💜")
    while True:
        await animeppaven()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm Extrerf donottouch.jpg")
        await asyncio.sleep(600) 

@bot.on(admin_cmd(pattern="gamerdp$"))
async def main(event):
    await event.edit("Activated Gamers Dp\nEnjoy 💜")
    while True:
        await animeppgame()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm Extrerf donottouch.jpg")
        await asyncio.sleep(600) 

@bot.on(admin_cmd(pattern="hackerdp$"))
async def main(event):
    await event.edit("Activated Hackers Dp\nEnjoy 💜")
    while True:
        await animepphack()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm Extrerf donottouch.jpg")
        await asyncio.sleep(600) 

@bot.on(admin_cmd(pattern="spacedp$"))
async def main(event):
    await event.edit("Activated Space Dp\nEnjoy 💜")
    while True:
        await animeppspace()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm Extrerf donottouch.jpg")
        await asyncio.sleep(600) 

@bot.on(admin_cmd(pattern="wallpapers$"))
async def main(event):
    await event.edit("Activated Wallappers on your DP\nEnjoy 💜")
    while True:
        await animeppwall()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(
            functions.photos.DeletePhotosRequest(
                await event.client.get_profile_photos("me", limit=1)
            )
        )
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm Extrerf donottouch.jpg")
        await asyncio.sleep(600) 
        
CMD_HELP.update(
    {
        "auto_dp": """**Plugin : **`auto_dp`
    
**Commands found in auto_dp are **
  •  `.batmandp`
  •  `.thordp`
  •  `.actressdp`
  •  `.animedp`
  •  `.avengersdp`
  •  `.gamerdp`
  •  `.hackerdp`
  •  `.spacedp`
  •  `.wallpapers`
**Function : **__Changes your profile pic every 10 minutes with the command you used(mean the batman or thor or blah blah blah......)__"""
    }
)
