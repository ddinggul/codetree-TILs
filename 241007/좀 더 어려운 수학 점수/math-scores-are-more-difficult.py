A_arr = input().split()
B_arr = input().split()

A_M = int(A_arr[0])
A_E = int(A_arr[1])

B_M = int(B_arr[0])
B_E = int(B_arr[1])

if (A_M > B_M) or (A_M == B_M and A_E > B_E):
    print("A")
elif B_M > A_M or (A_M == B_M and A_E < B_E):
    print("B")