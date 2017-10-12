def palindrome_permutation(string):
    string = sorted(string.lower().strip(' '))

    print(string)
    # Clean up extra whitespace
    i = 0
    for r in string:
        if r == ' ':
            string.remove(r)
        i = i + 1

    odd_sets = 0
    for s in string:
        instances = 0
        for t in string:
            if s == t:
                instances = instances + 1
        if instances % 2 != 0:
            odd_sets = odd_sets + 1

    if odd_sets > 1:
        return False
    return True

print(palindrome_permutation("tataco catat"))








