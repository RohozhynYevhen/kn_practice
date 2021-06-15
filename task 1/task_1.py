import re

string = input("Введите строку: ")

# Отделяем цифры от букв
nums = re.findall(r'\d+', string)
string = re.sub(r"\d+", "", string, flags=re.UNICODE)
# Массив строк преобразовываем в числа
nums = [int(i) for i in nums]

print("Строка без чисел:\n", string, sep='')
print("Массив чисел из строки:\n", nums, sep='')

# Функция меняющая в словах первую и последнюю букву на заглавные 
def cap(string):
     string, result = string.title(), ""
     for word in string.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]     #Удаление последнего пробела

print("\nЗамена первой и последней буквы в каждом слове на заглавные:\n", cap(string), sep='')

max_num = max(nums)
index_of_nums = nums.index(max_num)
print("\nМаксимальное значение в массиве:", max_num)
vals = []
# Формируем массив из чисел поднесенных в степень
for i in range(len(nums)):
    if i != index_of_nums:
        temp = nums[i] ** i
        vals.insert(i, temp)
print("Массив чисел поднесенных в степень:\n", vals, sep='')
