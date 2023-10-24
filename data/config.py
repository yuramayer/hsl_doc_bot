import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
DOC_PATH = str(os.getenv('DOC_PATH'))
RES_PATH = str(os.getenv('RES_PATH'))


admins_id = [
    ... # ADMIN TELEGRAM ID
]
