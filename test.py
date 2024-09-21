from unittest import result


def get_maximum_below(num_1:int, num_2:int, limit:int) -> int:
    """

    """

    result = 0
    if num_1 >= limit:
        result = num_2
    if num_2 >= limit:
        result = num_1
    if not (num_1 >= limit or num_2 >= limit):
        result = max(num_1,num_2)

    return result


print(get_maximum_below(4,2,1))