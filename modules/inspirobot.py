import time
import random
import base64
import subprocess
import requests

generate_url = "https://inspirobot.me/api?generate=true"
r = [8,6,7,5,3,0,9,1,2]
error_codes = [400,401,403,404,500]

def filename():
    return '/tmp/'+base64.b64encode((str(time.time())
            +str(random.choice(r))).encode('utf-8')).decode('utf-8')+"__inspirobot.jpg"

def generate():
    try:
        r = requests.get(generate_url)
        if(r.status_code == 200):
            content = requests.get(r.text)
            if(content.status_code not in error_codes):
                fname = filename()
                open(fname,'wb').write(content.content)
                return fname
    except Exception as e:
        print(type(e).__name__,e.args)
        return False
