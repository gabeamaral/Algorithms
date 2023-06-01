def sort(string):
    if len(string) < 2:
        return string
    pivot = string[0]
    less = [i for i in string if i < pivot]
    greater = [i for i in string if i > pivot]
    equal = [i for i in string if i == pivot]
    return sort("".join(less)) + "".join(equal) + sort("".join(greater))


def is_anagram(first_string, second_string):
    sorted_first = sort(first_string.lower())
    sorted_second = sort(second_string.lower())
    if (
        len(sorted_first) != len(sorted_second)
        or not first_string
        or not second_string
    ):
        return (sorted_first, sorted_second, False)
    else:
        return sorted_first, sorted_second, sorted_first == sorted_second
