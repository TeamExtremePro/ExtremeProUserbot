from urllib import request
import importlib
import os
import asyncio
from database import dloadsdb as extremedb, storagedb as storage, settingsdb as settings


modules = {}
classes = {}
imported = []
watchouts = []
cmds = {}


async def filestorage(client):
    filestorage = await storage.retrieve()
    if filestorage:
        for file in filestorage:
            try:
                msg = await client.get_messages(await settings.check_asset(), ids=file["File"])
                if not os.path.isdir(file["Path"]):
                    os.makedirs(file["Path"], 0o755)
                await client.download_media(msg, os.path.join(file["Path"], file["Name"]))
            except Exception:
                pass

async def loads():
    dloads = await extremedb.check_dload()
    if dloads:
        for mod in dloads:
            request.urlretrieve(mod["URL"], "./" + mod["Name"])
            try:
                imported.append(__import__(mod["Name"][0:-3]))
                print("Module is loaded: {}".format(
                    mod["Name"][0:-3].capitalize()))
            except ImportError as e:
                print("Module can not be loaded: {}\n\n{}".format(
                    mod["Name"][0:-3].capitalize(), e))
            os.remove(mod["Name"])
    base = os.path.basename(__name__)
    for f in os.listdir("/".join(base.split(".")[:2])):
        if not f.startswith("_") and f.endswith(".py"):
            try:
                f = os.path.join(".".join(base.split(".")[:2] + [f[:-3]]))
                imported.append(importlib.import_module(f))
                print("Module is loaded: {}".format(f[18::].capitalize()))
            except ImportError as e:
                print("Module can not be loaded: {}\n\n{}".format(
                    f[18::].capitalize(), e))
    imports()


def imports():
    for module in imported:
        for var in vars(module):
            if callable(vars(module)[var]):
                getclss = vars(module)[var]
                classes.update({getclss.__name__: {}})
                modules.update({getclss.__name__: {}})
                for cmd in vars(getclss):
                    if "watchout" in str(vars(getclss)[cmd]):
                        watchouts.append(vars(getclss)[cmd])
                    if callable(vars(getclss)[cmd]) and vars(
                            getclss)[cmd].__name__.endswith("xxx"):
                        modules[getclss.__name__].update(
                            {vars(getclss)[cmd].__name__.replace("xxx", ""): vars(getclss)[cmd]})
                        classes[getclss.__name__].update(
                            {vars(getclss)[cmd].__name__.replace("xxx", ""): vars(getclss)[cmd]})
                        cmds.update({vars(getclss)[cmd].__name__.replace(
                            "xxx", ""): vars(getclss)[cmd]})
                if not classes[getclss.__name__]:
                    del classes[getclss.__name__]
                    del modules[getclss.__name__]
