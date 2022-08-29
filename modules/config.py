import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "8934899"))
API_HASH = getenv("API_HASH", "bf3e98d2c351e4ad06946b4897374a1e")
BOT_TOKEN = getenv("BOT_TOKEN", "5774991710:AAF_S7qnoWM4wiZALxItDrMwpmGIlt7PTqk")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AgCNQ_Axs2yFugQ5UDEJTRr8TCl1tojsHkdYTNB-eMxOLHI28LGlNd-F0BKu_KIDQC5ks759SvJodI1ChKP7BAKXeevjH_lFHqpQHmlFFZlLH-kHvVTiAV4lYm5RO1_cLoF1XHqCiuoydVzpZ6ZJvorcF8LDjt4ft8VeiPSyiDeUeAPD16XkfjcJeK4oJVgCmjHjsGkrAsnuXp7b8FLNzAh8tUYOpGX1rAqRZeM4hPT5nAWwRWQ9NL1WcmmPTX1itnSRkQzo27uSwV1w2wUg8VSxZ6iAFvwZ8x0FDtzakl1wlAgwzEWRkM0ElwFxugyXpS1U7V2AgOHEttoS_b0SK8IaAAAAAUgh5wYA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2132412121").split()))
