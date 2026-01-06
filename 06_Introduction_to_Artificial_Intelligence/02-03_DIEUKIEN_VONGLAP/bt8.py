# Nhập dữ liệu từ người dùng
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
op = str(input("Nhập toán tử (+, -, *, /): "))

# Dùng if-elif để xử lý toán tử
if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    if b != 0:
        result = a / b
    else:
        result = "Không thể chia cho 0"
else:
    result = "Toán tử không hợp lệ"

print("Kết quả a", op, "b:", result)