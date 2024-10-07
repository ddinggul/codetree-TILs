A_arr = input().split()
B_arr = input().split()

A_A = int(A_arr[0])
A_S = A_arr[1]

B_A = int(B_arr[0])
B_S = B_arr[1]

if (A_A >= 19 and A_S == "M") or (B_A >= 19 and B_S == "M"):
    print(1)
else:
    print(0)