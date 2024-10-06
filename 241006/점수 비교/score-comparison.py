A_arr = input().split()
B_arr = input().split()

A_m = int(A_arr[0])
A_e = int(A_arr[1])

B_m = int(B_arr[0])
B_e = int(B_arr[1])

if A_m > B_m and A_e > B_e:
    print(1)
else:
    print(0)