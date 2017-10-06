# Determine if a string has all unique characters


def unique_chars(string):
    sorted_string = sorted(string)
    count = 0

    for i in sorted_string:
        if count == 0:
            count = count + 1
            continue

        if sorted_string[count] == sorted_string[count - 1]:
            return "This string does not contain all unique characters"

        count = count + 1
    return "This string contains all unique characters"

print(unique_chars("thiss"))