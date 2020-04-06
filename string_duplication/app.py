def string_duplication(str):
    result = ""
    test = list(str)
    for item in test:
        if item not in result:
            result += item
    return result


print(string_duplication("invigilation"))
