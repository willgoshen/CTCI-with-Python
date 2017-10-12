def palindrome_permutation(string):
    string = sorted(string)
    odd_sets = 0

    for i in string:
        if i == ' ':
            string.remove(i)
    for j in string:
        instance = 0
        for k in string:
            if j == k:
                instance = instance + 1
        if instance % 2 != 0:
            odd_sets = odd_sets + 1
    if odd_sets > 1:
        return False
    return True

print(palindrome_permutation("racecar"))