def rectangle_of_number(x: int | float) -> float:

    y = x**2

    result = round(y, 2)

    return result


print(rectangle_of_number(0.7))


def sum_of_two_numbers(a: int | float, b: int | float) -> float:

    result = a + b

    return result


print(sum_of_two_numbers(6, 5.5))


def integer_division(shared: int, divider: int) -> dict:

    answer = {"integer_part": shared // divider, "modulo": shared % divider}

    return answer


print(integer_division(6, 4))