arr = input().split()

a = arr[0]; b = arr[1]; c = arr[2]
result = 0

if a >= b:
    result = a
    if a >= c:
        result = a
    else:
        result = c
else:
    result = b
    if b >= c:
        result = b
    else:
        result = c

print(result)