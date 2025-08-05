def length(string):
    if string=="":
        return 0
    else:
        return 1 + length(string[1:])
print(length("Amaregouda"))