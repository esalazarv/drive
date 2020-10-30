import os
from dotenv import load_dotenv
from dotty_dict import dotty

# Load environment variables from .env file
load_dotenv()

config = dotty({
    # App configuration
    "app": {
        # App name
        "name": os.getenv("APP_NAME", "Feedma Drive"),
        # App version
        "version": os.getenv("APP_VERSION", "0.0.1"),
        # App debug mode
        "debug": os.getenv("APP_DEBUG", False)
    }
})
