def nan_interation(string):
    counter = 0
    string = string.replace("Not a ", "*")
    print(string)
    for symbol in string:
        if symbol == "*":
            counter += 1
    string = string.replace("*", "")
    if string != "NaN":
        return False
    else:
        return counter

print(nan_interation("Not a Not a NaN"))
