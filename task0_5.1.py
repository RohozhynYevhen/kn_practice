from random import randint
arr = [randint(-100,100) for i in range(30)]
odd_arr = []

def MaxNum(arr):
    m = arr[0]
    n = 0
    for i in range(1, len(arr)):
        if arr[i] > m:
            m = arr[i]
            n = i
    print("Max elem:", m, "\nPosition:", n)

def odd_list(arr, odd_arr):
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            odd_arr.insert(0, arr[i])

print("Array:", arr)
MaxNum(arr)
odd_list(arr, odd_arr)
temp = sorted(odd_arr, reverse = True)
print("New array:", temp)

