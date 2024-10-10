y = int(input())
a = ""
if y % 4 == 0:
    if y % 100 == 0:
        a = "true"
        if y % 400 != 0:
            a = "false"
        else:
            a = "true"
    else:
        a = "true"
else:
    a = "false"

print(a)