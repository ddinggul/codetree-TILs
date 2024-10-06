arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if a <= b and a <= c:
    a_1 = 1
else:
    a_1 = 0

if a == b == c:
    a_2 = 1
else:
    a_2 = 0

print(f"{a_1} {a_2}")