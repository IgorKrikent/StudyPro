from copy import copy


def middle_value(numbers: list) -> float:

    if numbers:

        result = sum(numbers, start=0) / len(numbers)

    else:

        result = 0

    return result


print(middle_value([3, 6, 15]))


def union_lists(first_list: list, second_list: list) -> list:

    union = [*first_list, *second_list]

    return union


print(union_lists([6, 8, 7], ['some', 'data']))
