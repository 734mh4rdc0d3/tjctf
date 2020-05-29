import string
lower = string.ascii_lowercase
key = {'q': 'a', 'w': 'b', 'e': 'c', 'r': 'd', 't': 'e', 'y': 'f', 'u': 'g', 'i': 'h', 'o': 'i', 'p': 'j',
 'a': 'k', 's': 'l', 'd': 'm', 'f': 'n', 'g': 'o', 'h': 'p', 'j': 'q', 'k': 'r', 'l': 's', 'z': 't',
  'x': 'u', 'c': 'v', 'v': 'w', 'b': 'x', 'n': 'y', 'm': 'z'}
que = input("Enter the encrypted flag: ")
sol = ""
for q in que:
    if(key.get(q,0)!=0):
        sol = sol + key[q]
    else:
        sol = sol + q
print("Flag: "+ sol)
