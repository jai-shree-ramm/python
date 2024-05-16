age = int(input("Enter you age: "))
if age < 0:
    print("Invalid age")
else:
    print("You", "can not" if age < 18 else "can", "vote in next election")