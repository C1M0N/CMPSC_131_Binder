# File: RA_02.py
# Author:  Doucheng Peng
# Section: YOUR_RECITATION_SECTION_HERE
# E-mail:  dbp5625@psu.edu

def get_code(input_number:int):
    if input_number % 2 == 0:
        if 2 <= input_number <= 5:
            return 131
        if 6 <= input_number <= 20:
            return "CMPSC"
        if input_number > 20:
            return 131
    else:
        return "CMPSC"

def joint(a:int, b:int, c:int):
    sum_2 = a + b
    sum_3 = a + b + c
    product_3 = a * b * c
    if sum_2 % 2 == 0:
        if (sum_2 % 7) % 2 != 0:
            return 1
        else:
            return 2
    if sum_3 % 2 != 0:
        if (product_3 % 11) % 2 == 0:
            return 3
        if product_3 // 11 >= 10:
            return 4
        else:
            return 5
    else:
        return 6







print(get_code(5))
print(get_code(96))
print(get_code(6))
print(get_code(2))


print (joint(4,4,9))
print (joint(1,2,12))
print (joint(5,2,3))