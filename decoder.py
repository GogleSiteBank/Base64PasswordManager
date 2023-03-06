import base64

def decode():
    encoded = input("Please enter the encoded string: ").encode("utf-8")
    return base64.standard_b64decode(encoded).decode("utf-8")

print(decode())