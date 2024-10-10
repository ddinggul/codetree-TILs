a_arr = input().split()
b_arr = input().split()
c_arr = input().split()
patient_A = []

a_z = a_arr[0]
a_t = int(a_arr[1])
a_s = ""


b_z = b_arr[0]
b_t = int(b_arr[1])
b_s = ""

c_z = c_arr[0]
c_t = int(c_arr[1])
c_s = ""

if a_z == "Y":
    if a_t >= 37:
        a_s = "A"
        patient_A.append(a_s)
    else:
        a_s = "C"
else:
    a_s = "D"

if b_z == "Y":
    if b_t >= 37:
        b_s = "A"
        patient_A.append(b_s)
    else:
        b_s = "C"
else:
    b_s = "D"

if c_z == "Y":
    if c_t >= 37:
        c_s = "A"
        patient_A.append(c_s)
    else:
        c_s = "C"
else:
    c_s = "D"

E_N = len(patient_A)

if E_N >= 2:
    sit = "E"
else:
    sit = "N"

print(sit)