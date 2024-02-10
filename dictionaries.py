from pprint import pprint


def dict_keyes(some_dict: dict) -> list:

    result = []

    for each in some_dict:

        result.append(each)

    print(result)

    return result


my_dict = {'first': 'value',
           'second': 'other value'}

dict_keyes(my_dict)


def merge_dicts(*dicts: dict) -> dict:

    united_dict: dict = {}

    for each in dicts:

        united_dict.update(each)

    return united_dict


one_more_dict = {'third': 'one more value',
                 'fourth': 'something new'}

pprint(merge_dicts(my_dict, one_more_dict))
