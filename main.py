import base64
import json
import random
import string

f  = open('manager.json', 'w')

stri = string.ascii_letters + string.digits
strs = string.ascii_letters + string.digits + string.punctuation + string.octdigits + string. hexdigits
digi = string.digits
amnts = 2,3
z = random.choice(amnts)
passa = "".join(random.choices(strs, k=25))
passw = passa.encode('utf-8')
rand = ''.join(random.choices(stri, k=25))
key = ""
def getKey():
    global key
    key = "".join(random.choices(strs, k=25))
getKey()

def encode():
    inp = str(input("Code ran successfully!\nEnter the passwords, emails, etc: ")).encode('utf-8')
    return inp

def decode():
    file = open('manager.json', 'r')
    read = file.read()
    r = base64.standard_b64decode(read)
    f = open("returned.txt", "w")
    f.write(r.decode('utf-8'))

digits = string.digits
randig = int(''.join(random.choices(digits, k=2)))
for i in range(999):
    k = int("".join(random.choices(digi, k=z)))
    randig -= 1
    if i != randig:
        if i != 998:
            a = string.ascii_letters + string.digits + string.punctuation + string.octdigits + string. hexdigits
            b = "".join(random.choices(a, k=k))
            b6 = base64.b64encode(b.encode('utf-8')).decode('utf-8')
            a1 = string.ascii_letters + string.digits + string.punctuation + string.octdigits + string. hexdigits
            b1 = "".join(random.choices(a, k=k))
            b1_bytes = b1.encode('utf-8')
            b61 = base64.standard_b64encode(b1_bytes).decode('utf-8')
            f.write(json.dumps({f"{b6}": f"{b61}"})  + ",\n")
        else:
            a = string.ascii_letters + string.digits + string.punctuation + string.octdigits + string. hexdigits
            b = "".join(random.choices(a, k=k))
            b6 = base64.b64encode(b.encode('utf-8')).decode('utf-8')
            a1 = string.ascii_letters + string.digits + string.punctuation + string.octdigits + string. hexdigits
            b1 = "".join(random.choices(a, k=k))
            b1_bytes = b1.encode('utf-8')
            b61 = base64.standard_b64encode(b1_bytes).decode('utf-8')
            f.write(json.dumps({f"{b6}==": f"{b61}"}) )
    else:
        if i != 997:
            b64 = base64.standard_b64encode(encode()).decode('utf-8')
            f.write(json.dumps({f"{b64}": f"{key}"}) + ",\n")
        else:
            b64 = base64.standard_b64encode(encode()).decode('utf-8')
            f.write(json.dumps({f"{b64}": f"{key}"}))

print(f"Your key is {key}")
decode()
f.close()