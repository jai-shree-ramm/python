try:
    int1 = int(input("Enter the first number: "))
    int2 = int(input("Enter the second number: "))
    print("Division: ", int1/int2)
except ValueError:
    print("Input must be numeric")
except ZeroDivisionError:
    print("Division with 0 not allowed")
