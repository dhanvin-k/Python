def RLE(input):
    output = ""
    previous_letter = input[0]
    count = 0
    for letter in input:
        if (letter == previous_letter):
            count += 1
        else:
            output += f"{previous_letter}{count}"
            previous_letter = letter
            count = 1
    output += f"{previous_letter}{count}"
    print(list)
    return output


def decode_RLE(input):
    output = ""
    revCount = ""
    for item in input[len(input)::-1]:
        if (item.isdigit()):
            revCount += f"{item}"
        else:
            count = revCount[len(revCount)::-1]
            output += item*int(count)
            revCount = ""
    return output[len(output)::-1]


print(RLE("wwwwuudd"))
print(decode_RLE("w10e2"))
