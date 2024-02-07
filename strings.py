def string_length(text: str) -> int:

    length = len(text)

    return length


print(string_length("some text"))


def united_string(*args: str) -> str:

    empty_string = ""

    for arg in args:

        empty_string += f'{arg} '

    result_string = empty_string.strip()

    return result_string


print(united_string("my", "name", "is", "Igor"))
