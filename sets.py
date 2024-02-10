def union_sets(first_set: set, second_set: set) -> set:

    united_set = first_set.union(second_set)

    return united_set


print(union_sets({90, 7, 7.8}, {90, 8, 0}))


def check_sets_instance(main_set: set, sub_set: set) -> bool:

    return sub_set.issubset(main_set)


print(check_sets_instance(main_set={8, 9, 10}, sub_set={9, 10}))
