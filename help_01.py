from __future__ import annotations


def get_max(num_1: int | float, num_2: int | float) -> int | float:
    if num_1 < num_2:
        return num_2
    else:
        return num_1

def get_num(num: int | float, bound_1: int | float, bound_2: int | float) -> int | float:
    if bound_1 <= num <= bound_2 or bound_2 <= num <= bound_1:
        return num
    if num > get_max(bound_1, bound_2):
        return get_max(bound_1, bound_2)



input_1 = input("number plz")
input_2 = input("bound1 plz")
input_3 = input("bound2 plz")

print(get_num(input_1, input_2, input_3))

