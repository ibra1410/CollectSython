import os
import json
import requests
import subprocess

A = '\033[1;34m'  # ازرق
X = '\033[1;33m'  # اصفر

# إدخال توكن البوت والايدي مباشرة
api_id = 27455984
api_hash = '62d5f68ce2e9189636967120220f5755'
bot_token = '6615217281:AAG-kS0Mwo22uPvtOL4aLwxAuymAyitHnfo'
DEVLOO = '6946908675'
MAX_ACCOUNTS = 10

filename = 'sython.json'

data = {
    'api_id': api_id,
    'api_hash': api_hash,
    'bot_token': bot_token,
    'DEVLOO': DEVLOO,
    'MAX_ACCOUNTS': MAX_ACCOUNTS
}

with open(filename, 'w') as f:
    json.dump(data, f)

response = requests.get("https://raw.githubusercontent.com/sythontm/CollectSython/main/sython-telethon-cl.py")

with open('sython-telethon-cl.py', 'w') as file:
    file.write(response.text)

responsee = requests.get("https://raw.githubusercontent.com/sythontm/CollectSython/main/sythonkalb.py")

with open('sythonkalb.py', 'w') as file:
    file.write(responsee.text)

responseee = requests.get("https://raw.githubusercontent.com/sythontm/CollectSython/main/run.py")

with open('run.py', 'w') as file:
    file.write(responseee.text)

os.system('python3 sython-telethon-cl.py')
