def bubbleSort(arr, n):
    l = list(arr)
    for i in range(n):
        for j in range(n-i-1):
            if (l[j]>l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]
    print("Bubble Sort:", l)

def insertionSort(arr, n):
    l = list(arr)
    for step in range(1, n):
        key = l[step]
        j = step - 1
        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]
            j = j - 1
        l[j+1] = key
    print("Insertion Sort:", l)

def selectionSort(arr, n):
    l = list(arr)
    for step in range(n):
        min_i = step
        for i in range(step + 1, n):
            if l[i] < l[min_i]:
                min_i = i
        l[step], l[min_i] = l[min_i], l[step]
    print("Selection Sort:", l)
    
n = int(input("Enter length of l: "))
arr = [int(input(f"l[{i}]: ")) for i in range(n)]

bubbleSort(arr, n)
insertionSort(arr, n)
selectionSort(arr, n)
