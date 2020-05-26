from pwn import process
import time
from itertools import product

sleeptime = 0.001

for comb in product(['1', '2', '3', '4'] , repeat = 7):
	p = process("./gym")

	text = p.recv()
	p.sendline(bytes(comb[0], "ascii"))
	time.sleep(sleeptime)
	text = p.recv()
	p.sendline(bytes(comb[1], "ascii"))
	time.sleep(sleeptime)
	text = p.recv()
	p.sendline(bytes(comb[2], "ascii"))
	time.sleep(sleeptime)
	text = p.recv()
	p.sendline(bytes(comb[3], "ascii"))
	time.sleep(sleeptime)
	text = p.recv()
	p.sendline(bytes(comb[4], "ascii"))
	time.sleep(sleeptime)
	text = p.recv()
	p.sendline(bytes(comb[5], "ascii"))
	time.sleep(sleeptime)
	text = p.recv()
	p.sendline(bytes(comb[6], "ascii"))
	time.sleep(sleeptime)
	text = p.recv()
	p.kill()
	if("didn't reach my goal" not in str(text)):
		print(comb)
		break