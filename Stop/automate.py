from pwn import process
import time

sleeptime = 0.01
answers = []
for i in range(ord("a") , ord("z")+1):
	opdict = {
		"Country Capitals": "",
		"Electronics and Gadgets": "",
		"Sports": "",
		"Things You Keep Hidden": "",
		"Top Broadway Shows": "",
	}
	for j in range(5):
		p = process("./stop")
		p.recv()
		time.sleep(sleeptime)
		p.sendline(chr(i))
		time.sleep(sleeptime)
		p.recv()
		p.sendline(list(opdict.keys())[j])
		time.sleep(sleeptime)
		opdict[list(opdict.keys())[j]] = (str(p.recv())[20:])[:-3]

	answers.append((chr(i) , opdict))

for char in answers:
	print("letter: ",char[0])
	print(char[1])