arr = input().split()

a = int(arr[0])
b = int(arr[1])

if a < b :
    p1 = 1
else:
    p1 = 0

if a == b:
    p2 = 1
else:
    p2 = 0

print(f"{p1} {p2}")