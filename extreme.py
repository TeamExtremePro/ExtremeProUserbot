MONGOCLIENT = MongoClient(MONGO_URI, 27017, serverSelectionTimeoutMS=1)

BOTLOG = (os.environ.get("BOTLOG") == 'True')

BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID")) if BOTLOG else 0

PM_AUTO_BAN = (os.environ.get("PM_AUTO_BAN") == 'True')

def is_mongo_alive():
    try:
        MONGOCLIENT.server_info()
    except BaseException as e:
        print(e)
        return False
    return True


COUNT_MSG = 0

USERS = {}

COUNT_PM = {}

LASTMSG = {}

CMD_HELP = {}
