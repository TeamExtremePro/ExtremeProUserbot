#    This file is part of ExtremeProUserbot.

#    ExtremeProUserhpt is free userbot: you can redistribute it and/or modify by permisson
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    AmanPandey is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with ExtremeProUserbot.  If not, see <https://www.gnu.org/licenses/>.
#    Kangers tum kang toh kar lete ho but banane me time aur mehnat lagta h 


from database.mongo import cli
import logging


cli = cli["ExtremePro"]["AntiPM"]


async def set_antipm(opt):
    return cli.insert_one({"AntiPM": opt})

async def approve(user):
    return cli.insert_one({"Approved": user})

async def set_limit(digit):
    return cli.insert_one({"Limit": digit})

async def set_notif(opt):
    return cli.insert_one({"Notifications": opt})

async def set_sblock(opt):
    return cli.insert_one({"SuperBlock": opt})

async def check_antipm():
    return (False if not cli.find_one({"AntiPM": {"$exists": True}})
        else cli.find_one({"AntiPM": {"$exists": True}})["AntiPM"])

async def check_limit():
    return (3 if not cli.find_one({"Limit": {"$exists": True}})
        else cli.find_one({"Limit": {"$exists": True}})["Limit"])
    
async def check_sblock():
    return (False if not cli.find_one({"SuperBlock": {"$exists": True}})
        else cli.find_one({"SuperBlock": {"$exists": True}})["SuperBlock"])

async def check_notifs():
    return (True if not cli.find_one({"Notifications": {"$exists": True}})
        else cli.find_one({"Notifications": {"$exists": True}})["Notifications"])

async def check_approved(user):
    return cli.find_one({"Approved": user})

async def delete(obj):
    return cli.delete_one({obj: {"$exists": True}})

async def disapprove(user):
    return cli.delete_one({"Approved": user})
