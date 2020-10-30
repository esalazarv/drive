import os
from dotenv import load_dotenv
from dotty_dict import dotty
load_dotenv()

config = dotty({
    "app": {
        "name": os.getenv("APP_NAME", "Feedma Drive"),
        "debug": os.getenv("APP_DEBUG", False)
    }
})