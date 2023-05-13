import base64, random, string

def generateFileName():
    return "output" + "".join(random.choices(string.ascii_letters, k=12)) + ".txt"
f = open(generateFileName(), "a")
print("File will be saved to \"%s\"" % f.name)


def getRandomstring():
    randomint = random.randint(1, 50)
    return "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=randomint))

stopInt = random.randint(0,998)


def getPasswords():
    return base64.b64encode((input("Passwords, emails, etc: ").encode('utf-8'))).decode('utf-8')

def main():
    print("Writing lines...")
    for i in range(999):
        if i == stopInt:
            key = getRandomstring()
            f.write(key)
            f.write(getPasswords())
            endKey = getRandomstring()
            f.write(endKey)
            print("Your First Key:\n%s\nYour second Key:\n%s" % (key, endKey))
        else:
            f.write(getRandomstring())
    
if __name__ == "__main__":
    main()
