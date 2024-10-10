arr = input().split()

a = arr[0]; b = arr[1]; c = arr[2]
result = 0

if a >= b:
    if a >= c:
        result = a
    else:
        result = c
elif b >= a:
    if b >= c:
        result = b
    else:
        result = c
else:
    if c >= a:
        result = c
    else:
        result = b

print(result)