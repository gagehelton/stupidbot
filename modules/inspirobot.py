import os
import time
import random
import base64
import subprocess

generate_url = "https://inspirobot.me/api?generate=true"

def generate():
    r = [8,6,7,5,3,0,9,1,2]
    contents = subprocess.check_output(['curl',subprocess.check_output(['curl',generate_url])])
    fname = '/tmp/'+base64.b64encode((str(time.time())+str(random.choice(r))).encode('utf-8')).decode('utf-8')+"__inspirobot.jpg"
    try:
        open(fname,'wb').write(contents)
        return fname
    except Exception as e:
        print(type(e).__name__,e.args)
        return False    
