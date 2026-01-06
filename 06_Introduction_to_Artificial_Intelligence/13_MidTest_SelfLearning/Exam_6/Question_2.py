'''
Đề 7 Luyện Tập Python (Cơ Bản)Câu 1 (Vấn đề chung): Đảo ngược Chuỗi và Kiểm tra Đối xứng
    Yêu cầu: Viết một hàm Python có tên là kiem_tra_doi_xung(chuoi) nhận vào một chuỗi (string). 
    Hàm phải kiểm tra xem chuỗi đó có phải là chuỗi đối xứng (palindrome - đọc xuôi hay đọc ngược đều như nhau) hay không. 
    Hàm trả về True hoặc False.
    Ví dụ (Input/Output):
        Input 1: "madam"
        Output mong đợi 1: True
        Input 2: "racecar"
        Output mong đợi 2: True
        Input 3: "hello"
        Output mong đợi 3: False

Câu 2 (Lập trình hướng đối tượng - OOP): Lớp Diem và Phép cộng Đối tượng 
    Yêu cầu: Định nghĩa lớp Diem (Point) để biểu diễn tọa độ và hỗ trợ toán tử cộng.
    1. Lớp Diem (Point)Thuộc tính: x (float), y (float) - tọa độ điểm.
        Phương thức khởi tạo __init__: Nhận và gán giá trị cho x và y.
        Phương thức đặc biệt __add__(other):
            Mục đích: Hỗ trợ toán tử cộng (+) giữa hai đối tượng Diem.
            Cách hoạt động: Cộng tọa độ x với x và y với y của hai điểm.
            Giá trị trả về: Một đối tượng Diem mới là kết quả của phép cộng
'''

# Câu 2
class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other: Diem):
        newX = self.x + other.x
        newY = self.y + other.y
        return Diem(newX, newY)

d1 = Diem(1,2)
d2 = Diem(2,3)

d3 = d1.__add__(d2)

print(d3.x, d3.y)