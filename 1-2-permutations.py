def permutations(s1, s2):
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)

    if sorted_s1 == sorted_s2:
        return "'{}' is a permutation of '{}'".format(s1, s2)

    return "'{}' is not a permutation of '{}'".format(s1, s2)


print(permutations("this", "histy"))