def urlify(string):
    url = list(string)
    index = 0
    for i in url:
        if i == " ":
            url[index] = "%20"
        index = index + 1

    url = ''.join(url)
    return url

print(urlify("Mr. Will Goshen"))
