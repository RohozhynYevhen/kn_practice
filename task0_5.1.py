from random import randint
arr = [randint(-100,100) for i in range(30)]
odd_arr = []

# I prefer this macros
max_arr = max(arr)
index_of_max = arr.index(max_arr)
print("Max: ", max_arr, " Index: ", index_of_max)
# https://www.programiz.com/python-programming/methods/built-in/max

def odd_list(arr, odd_arr):
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            odd_arr.insert(0, arr[i])

print("Array:", arr)
odd_list(arr, odd_arr)
temp = sorted(odd_arr, reverse = True)
print("New array:", temp)

