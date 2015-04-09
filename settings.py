try:
    from secrets import *
except ImportError:
    import sys
    sys.exit('secrets.py settings file not found. Please run `prepare.sh` to create one.')

SERVER_URLS = (
    "https://www.onepercentclub.com",
    "https://crowdfunding.gent",
    "https://hetluktons.nl"
)

STREAM_SERVER = "https://stream.onepercentclub.com"
