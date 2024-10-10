arr = input().split()

a = int(arr[0]); b = int(arr[1]); c = int(arr[2])
result = 0

if a >= b:
    if a >= c:
        result = a
    else:
        result = c
else:
    if b >= c:
        result = b
    else:
        result = c

print(result)