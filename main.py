import hashlib
import json
import itertools
data = {}
def convert_tuple(c_tuple): 
    str=''.join(c_tuple) 
    return str
data['hash'] = []   
userData = input()
for i in range(1,16):
    mas = itertools.product('0123456789', repeat=i)
    print(i)
    for i in mas:
        data['hash'].append({
            convert_tuple(i): hashlib.md5(convert_tuple(i).encode()).hexdigest(),
        })
        if userData == hashlib.md5(convert_tuple(i).encode()).hexdigest():
            print(convert_tuple(i))
            break
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
