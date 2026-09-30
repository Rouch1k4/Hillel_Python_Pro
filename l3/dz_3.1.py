
# 1.Рядки (Strings):

"""
text = "PythonBest"
def function_length(text) :
    length = len(text)
    return
print(function_length(text))

"""

"""
a = "Python"
b = "Pro"
def connect_strings (a, b) :
    connect = (a + " " + b)
    return connect
print(connect_strings(a, b))

"""
# 2.Числа (Int/float):

"""
number = 5
def square (number) :
    responce = number ** 2
    return responce
print(square(number))

"""

"""
a = 20
b = 10
def count_numbers (a, b) :
    responce = a + b
    return responce
print(count_numbers(a, b))

"""

"""
a = 33
b = 5

def div_numbers (a, b) :
    responce = a // b
    rest = a % b
    return responce, rest
print(div_numbers(a, b))
"""

# 3. Списки (Lists)

"""
num = [3, 8, 9, 11, 15]

def average (num) :
    responce = sum(num) / len(num)
    return responce
print(average(num))

"""

"""
list1 = [3, 8, 9, 11, 15]
list2 = [8, 9, 11, 13, 2]

def common (list1, list2) :
    set1 = set(list1)
    set2 = set(list2)
    common = set1.intersection(set2)
    return common
print(common(list1, list2))

"""

# 4. Словники (Dictionaries):

"""
d = {"Name" : "Vasya", "Age" : 67, "Nationality" : "USA" }

def search_keys (d) :
    for key in d.keys() :
       print(key)

print(search_keys(d))

"""

"""

d1 = {"Phone" : "+380666752166", "eMail": "<rommeik@gmail.com>"}
d2 = {"Name" : "Vasya", "Age" : 67, "Nationality" : "USA" }

def connect_dicts (d1, d2) :
    result = d1 | d2
    return result
print(connect_dicts(d1, d2))

"""
# 5. Множини (Sets):

"""
a = {6, 7, 2}
b = {1, 5, 8}

def connect_sets (a, b) :
    result = a | b
    return result

print(connect_sets(a, b))

"""

"""
a = {2, 5, 6}
b = {6, 7, 2, 5}

def verif_subbset (a, b) :
    result = (a.issubset(b))
    return result
print(verif_subbset(a, b))

"""

# 6. Умовні вирази та цикли:

"""
number = 7
def check_number (number) :
    if number % 2 == 0 :
        print("Число парне")
    else :
        print("Число непарне")

check_number(number)

"""
"""
nums = [2, 4, 3, 8, 9, 11, 15]

def even_list (nums) :
    result = []
    for numbers in nums :
        if numbers % 2 == 0 :
            result.append(numbers)

    return result
print(even_list(nums))


"""
# 7. Написати лямбда-функцію визначальну парне/непарне.

"""
x = 6
even = lambda x: "Парне" if x % 2 == 0 else "Непарне"
print(even(x))

"""











