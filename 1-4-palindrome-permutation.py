def palindrome_permutation(string):
    string = sorted(string.lower().strip(' '), reverse=True)
    print(string)

    instance = 1
    i = 0
    odd_sets = 0
    for _ in string:
        if i == 0:
            continue
        elif string[i] == string[i - 1]:
            instance = instance + 1
        else:
            if instance % 2 != 0:
                odd_sets = odd_sets + 1
                if odd_sets > 1:
                    return False
            instance = 1
        i = i + 1
    return True

print(palindrome_permutation("racecar"))