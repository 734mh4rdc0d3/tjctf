f = open('song.txt').read()

l = {'1':'A', '2':'B', '3':'C', '4':'D', '5':'E', '6':'F', '7':'G'}
chords = {'A': '0112', 'B': '2110', 'C': '1012', 'D': '020', 'E': '0200', 'F': '1121', 'G': '001', 'a': '0122', 'b': '2100', 'c': '1002', 'd': '010', 'e': '0100', 'f': '1011', 'g': '000'}


s = ''
for i in f:
	c1, c2 = hex(ord(i))[2:]
	if c1 in l:
		c1 = l[c1]
	if c2 in l:
		c2 = l[c2]
	s += chords[c1] + chords[c2]

open('notes.txt', 'w').write(s)