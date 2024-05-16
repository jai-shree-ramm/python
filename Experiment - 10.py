import shutil
while True:
    try:
        src = input("Enter source: ")
        dest = input("Enter destination: ")
        print("1. Using shutil")
        print("2. Copy content")
        mode = int(input("Enter mode: "))
        if mode==1:
            shutil.copy(src, dest)
        elif mode==2:
            with open(src) as f:
                content = f.read()
            with open(dest) as f:
                f.write(content)
        else:
            continue
        print("File copied")
        break
    except:
        print("Something went wrong!\n")
