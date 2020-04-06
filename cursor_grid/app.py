def cursor_grid(a, x, y, str):
    output = [x, y]
    for action in str:
        if action == "U":               # checking if cursor action is UPPER
            if output[0] != 0:
                output[0] += -1
        elif action == "D":             # checking if cursor action is DOWN
            if output[0] != a-1:
                output[0] += 1
        elif action == "L":             # checking if cursor action is LEFT
            if output[1] != 0:
                output[1] += -1
            else:                           # execting LEFT boundary action
                output[1] = a-1
        else:                           # checking if cursor action is RIGHT
            if output[1] != a-1:
                output[1] += 1
            else:                           # execting RIGHT boundary action
                output[1] = 0
    return output


print(cursor_grid(3, 0, 0, "RDD"))
print(cursor_grid(3, 1, 0, "LLUU"))
