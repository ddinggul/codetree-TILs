arr = input().split()
m = int(arr[0])
f = int(arr[1])

if m >= 90:
    if f >= 95:
        print(100000)
    elif f >= 90 and f < 95:
        print(50000)
    else:
        print(0)
else:
    print(0)