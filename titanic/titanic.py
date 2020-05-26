import hashlib

subtitle = open("subtitle.srt")
found = False

for line in subtitle:
	line = line.split(" ")
	for word in line:
		word = "tjctf{"+word+"}"
		if(hashlib.md5((word.lower()).encode()).hexdigest() == "e246dbab7ae3a6ed41749e20518fcecd"):
			print(word.lower())
			found = True
			break
	if(found):
		break

subtitle.close()

