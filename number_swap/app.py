def number_swap(str):
    temp = list(str)
    for index1, item1 in enumerate(temp):
        if item1.isdigit() and index1 < len(temp)-2:
            for index2, item2 in enumerate(temp[index1+1:], index1+1):
                if item2.isdigit():
                    sub_string = temp[index1+1:index2]
                    if all([not i.isspace() for i in sub_string]) and any([j.isalpha() for j in sub_string]):
                        swap = temp[index1]
                        temp[index1] = temp[index2]
                        temp[index2] = swap
                    break
    return "".join(temp)


print(number_swap("acb3gh85-ds4"))
