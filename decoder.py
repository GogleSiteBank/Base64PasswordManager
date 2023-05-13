from tkinter import filedialog
import base64

def main():
    firstKey = input("Input first key: ")
    secondKey = input("Input second key: ")
    fileInput = filedialog.askopenfile()
    content = str(fileInput.read())
    firstDecode = content.split(firstKey)[1]
    print("Output: %s"  % base64.b64decode(firstDecode.split(secondKey)[0].encode()).decode())

if __name__ == "__main__":
    main()
