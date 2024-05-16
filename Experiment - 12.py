import requests, webbrowser

url = input("Enter url: ")
res = requests.get(url)

try:
    res.raise_for_status();
    path = input("Enter file path: ")
    with open(path, "w") as f:
        f.write(res.text)
    webbrowser.open(path)
    print("Url opened locally")
except:
    print("Error")
