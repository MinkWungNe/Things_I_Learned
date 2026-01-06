# Nhập 2 ma trận A, B
nA = int(input("Nhập số dòng ma trận A: "))
mA = int(input("Nhập số cột ma trận A: "))

A = []
print("Nhập các phần tử ma trận A:")
for i in range(nA):
    row = list(map(int, input(f"Nhập dòng {i + 1} (cách nhau bởi dấu cách): ").split()))
    A.append(row)

nB = int(input("Nhập số dòng ma trận B: "))
mB = int(input("Nhập số cột ma trận B: "))

B = []
print("Nhập các phần tử ma trận B:")
for i in range(nB):
    row = list(map(int, input(f"Nhập dòng {i + 1} (cách nhau bởi dấu cách): ").split()))
    B.append(row)  

# Cộng hai ma trận A và B
if nA == nB and mA == mB:
    C = []
    for i in range(nA):
        row = []
        for j in range(mA):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    
    print("Ma trận C = A + B là:")
    for row in C:
        print(" ".join(map(str, row)))
else:
    print("Không thể cộng hai ma trận vì kích thước không khớp.")

# Hàm tính hoán vị
def hoanvi(A, B):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j], B[i][j] = B[i][j], A[i][j]
    return A, B

# Hoán vị hai ma trận A và B nếu kích thước giống nhau
if nA == nB and mA == mB:
    A, B = hoanvi(A, B)
    print("Ma trận A sau khi hoán vị:")
    for row in A:
        print(" ".join(map(str, row)))
    print("Ma trận B sau khi hoán vị:")
    for row in B:
        print(" ".join(map(str, row)))