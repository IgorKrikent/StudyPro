def is_double_number(number: int) -> bool:

    if number % 2:

        print(f'{number} is not double')

        return False

    print(f'{number} is double')

    return True


is_double_number(11)


def only_doubles_numbers(numbers_list: list[int]) -> list[int]:

    result = []

    for each in numbers_list:

        if is_double_number(each):

            result.append(each)

    return result


print(only_doubles_numbers([4, 7, 5, 8, 10]))
