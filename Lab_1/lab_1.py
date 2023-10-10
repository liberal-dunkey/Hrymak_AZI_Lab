import string
abc = string.ascii_lowercase
s = open('og.txt', 'r', encoding="utf-8")
alph = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
f = open("cipher.txt", 'w+', encoding="utf-8")
key = 9
stext = s.read().lower()
dlist = list()
for i in stext:
    try:
        try:
            idx = alph.index(i)
            new_idx = (idx + key) % 33
            dlist.append(alph[new_idx])
        except:
            idx = abc.index(i)
            new_idx = (idx + key) % 26
            dlist.append(abc[new_idx])
    except:
        dlist.append(i)
        continue
flist = ''.join(dlist)
f.write(flist)
f.close()