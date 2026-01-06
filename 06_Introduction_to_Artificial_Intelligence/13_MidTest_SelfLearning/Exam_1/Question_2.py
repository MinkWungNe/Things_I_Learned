'''
Đề 1
Câu 1 (Vấn đề chung): Xử lý Tên và Tuổi
    Viết một chương trình Python yêu cầu người dùng nhập Họ và Tên đầy đủ (ví dụ: "Nguyễn Văn A") và Năm Sinh (ví dụ: 1990).
    Chương trình phải thực hiện các bước sau:
    Xử lý Chuỗi: Tách họ, tên đệm (nếu có), và tên riêng, sau đó in ra tên riêng và chữ cái đầu tiên của họ, tên đệm.
    Toán tử & Kiểu dữ liệu: Tính và in ra tuổi hiện tại của người dùng (giả sử năm hiện tại là 2025).

Câu 2 (Lập trình hướng đối tượng - OOP): Lớp SanPham
    Định nghĩa một lớp có tên là SanPham (Product) với các thuộc tính: ten (string), ma_hang (string), và gia_niem_yet (float).
    Triển khai phương thức khởi tạo __init__ để gán giá trị cho các thuộc tính.
    Triển khai một phương thức tinh_gia_ban(ty_le_lai) nhận vào một float ty_le_lai và trả về giá bán cuối cùng.
'''

# Câu 2:
class SanPham:
    def __init__(self, ten, ma_hang, gia_niem_yet):
        self.ten = ten
        self.ma_hang = ma_hang
        self.gia_niem_yet = gia_niem_yet
        
    def tinh_gia_ban(self, ti_le_lai):
        return self.gia_niem_yet * (1+ti_le_lai)
    
# Test
laptop = SanPham('Dell', 'Dell01', 15000000)
print(laptop.gia_niem_yet, laptop.tinh_gia_ban(.20))