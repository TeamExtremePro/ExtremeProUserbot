import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from userbot.mainfiles.configs.heroku import Var as Config
else:
    from local_config import Development as Config


Var = Config
