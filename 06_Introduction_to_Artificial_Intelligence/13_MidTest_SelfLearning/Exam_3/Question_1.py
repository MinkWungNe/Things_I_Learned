'''
Đề 3 Luyện Tập Python
Câu 1 (Vấn đề chung): Lọc Danh sách Số Chẵn/Lẻ 🔢
    Yêu cầu: Viết một hàm Python có tên là loc_so_chan_le(danh_sach) nhận vào một list các số nguyên. 
    Hàm phải trả về một tuple gồm hai list: list đầu tiên chứa các số chẵn, list thứ hai chứa các số lẻ.
    Ví dụ (Input/Output):
        Input: [12, 5, 8, 17, 4, 9]
        Output mong đợi: ([12, 8, 4], [5, 17, 9])

Câu 2 (Lập trình hướng đối tượng - OOP): Lớp NhanVien 🧑‍💼
Yêu cầu: Định nghĩa lớp NhanVien (Employee) và các phương thức sau:
    1. Phương thức khởi tạo __init__
        Mục đích: Khởi tạo đối tượng NhanVien với các thuộc tính: ma_so (string), ten (string), và luong_co_ban (float).
        Tham số: self, ma_so_nv, ten_nv, luong_cb.
    2. Phương thức tinh_thuong(ty_le_thuong)
        Mục đích: Tính và trả về tiền thưởng dựa trên lương cơ bản.
        Tham số: self, ty_le_thuong (float, ví dụ: 0.1 cho 10%).
        Cách hoạt động: Tiền thưởng = luong_co_ban $\times$ ty_le_thuong.
        Giá trị trả về: Tiền thưởng (float).
'''

# Câu 1
def Odd_Or_Even(numList):
    oddList = []
    evenList = []
    numTuple = ()

    for num in numList:
        if num % 2 ==0:
            evenList.append(num)
        else:
            oddList.append(num)
    
    numTuple = (evenList, oddList)
    return numTuple

print(Odd_Or_Even([12, 5, 8, 17, 4, 9]))