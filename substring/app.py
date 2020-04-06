def substring(str):
    k = int(str[0])
    highest_length = 0
    longest_string = ""
    newStr = str[1:]
    for start_point in range(0, len(newStr)):
        for end_point in range(len(newStr), start_point, -1):
            check = set(newStr[start_point:end_point])
            if len(check) == k and len(newStr[start_point:end_point]) > highest_length:
                highest_length = len(newStr[start_point:end_point])
                longest_string = newStr[start_point:end_point]
    return longest_string


print(substring("4abbaccdhhll"))
