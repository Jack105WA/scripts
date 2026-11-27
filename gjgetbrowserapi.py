import requests as rq

print("jacks gjget (gdbrowser api ver)")
print(" ")
getoption = int(input("1: accounts").strip())

url = "https://gdbrowser.com/api"

if getoption == 1:
    
    id = str(input("account id or name").strip())
    url = url + "/profile/" + id
    req = rq.get(url)
    print (req.text)



input()