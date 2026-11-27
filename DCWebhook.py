import requests as rq
import random

webhk = input("Webhook URL:  ").strip()
option = int(input("1. send message | 2. gd user info | 3. Random greeting").strip())
secret = "Wmfd2893gb7"

if option == 1:
    content = input("Type a message: ").strip()
    data = {
        "content": content,
    }
    response = rq.post(webhk, json=data)

if option == 2:
    targetid = input("Enter AccountID: ").strip()
    if targetid == "":
        targetid = 31436582
    else:
        targetid = int(targetid)

    url = "https://www.boomlings.com/database/getGJUserInfo20.php"
    params = {"secret": secret, "targetAccountID": targetid }
    headers = {
    "User-Agent": ""
    }

    req = rq.post(url, data=params, headers=headers)
    datagd = {
        "content": req,
    }

    response = rq.post(webhk, datagd)

if option == 3:
    textlist = ["Hello", "Hola", "Hej", "Bonjour"]
    
    data = {
        "content": random.choice(textlist),
    }
    response = rq.post(webhk, json=data)