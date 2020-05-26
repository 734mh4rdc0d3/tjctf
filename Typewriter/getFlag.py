import string
lower = string.ascii_lowercase
key = {'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p', 'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 
'g', 'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z', 'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n', 'z': 'm'}
que = input("Enter the encrypted flag: ")
sol = ""
for q in que:
    if(key.get(q,0)!=0):
        sol = sol + key[q]
    else:
        sol = sol + q
print("Flag: "+ sol)