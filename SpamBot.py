import time
import requests
import threading as tr


IDString = ""
AccountToken = ""
TimesRepeat = 2
TimeWait = 3
Message = """Test"""



def SendMessage():
    requests.post(f'https://discord.com/api/v9/channels/'+ IDString +'/messages', data = {"content": Message}, headers={'authorization': AccountToken})

def SendMessagereREP():
    while True:
        TIMES = int(TimesRepeat)
        while TIMES > 0:
            SendMessage()
            TIMES -= 1
        time.sleep(TimeWait)
        


tr.Thread(target=SendMessagereREP).start()