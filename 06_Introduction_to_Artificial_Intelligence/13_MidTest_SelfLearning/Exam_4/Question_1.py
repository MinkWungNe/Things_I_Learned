'''
Đề 4 Luyện Tập Python
Câu 1 (Vấn đề chung): Tính Tổng các Chữ số 
    Yêu cầu: Viết một hàm Python có tên là tinh_tong_chu_so(n) nhận vào một số nguyên dương $n$ bất kỳ. 
    Hàm phải tính và trả về tổng các chữ số của số đó.
    Ví dụ (Input/Output):Input: 12345
    Output mong đợi: 15 (1 + 2 + 3 + 4 + 5)

Câu 2 (Lập trình hướng đối tượng - OOP): Lớp TaiKhoanNganHang 💰
    Yêu cầu: Định nghĩa lớp TaiKhoanNganHang (Bank Account) để thực hiện các thao tác giao dịch cơ bản.
    1. Phương thức khởi tạo __init__
        Mục đích: Khởi tạo đối tượng với các thuộc tính: so_tai_khoan (string), ten_chu_tai_khoan (string), và so_du (float, mặc định là 0.0).
        Tham số: self, so_tai_khoan_tk, ten_chu_tai_khoan_tk.

    2. Phương thức nap_tien(so_tien)
        Mục đích: Tăng số dư tài khoản.
        Cách hoạt động: Cộng so_tien vào so_du. 
        Phải kiểm tra: nếu so_tien <= 0$, in ra thông báo lỗi và không thay đổi số dư.

    3. Phương thức rut_tien(so_tien)
        Mục đích: Giảm số dư tài khoản.
        Cách hoạt động: Trừ so_tien khỏi so_du. 
        Phải kiểm tra: nếu so_tien <= 0$ hoặc so_tien < so_du, in ra thông báo lỗi và không thay đổi số dư.
'''

#Câu 1
num = int(input('Enter a number (>0):'))

num = str(num)
sum = 0
for char in num:
    sum += int(char)

print('Sum from each num in "{:s}": {:.0f}'.format(num, sum))