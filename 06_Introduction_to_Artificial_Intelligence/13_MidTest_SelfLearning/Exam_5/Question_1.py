'''
Đề 5 Luyện Tập Python
Câu 1 (Vấn đề chung): Tìm Các Phần tử Duy nhất 
    Yêu cầu: Viết một hàm Python có tên là tim_phan_tu_duy_nhat(danh_sach) nhận vào một list bất kỳ. 
    Hàm phải trả về một list mới chỉ chứa các phần tử duy nhất (không lặp lại) từ danh sách đầu vào, giữ nguyên thứ tự xuất hiện lần đầu của các ph.tử.
    Ví dụ (Input/Output):
        Input: ['a', 'b', 'c', 'a', 'd', 'b']
        Output mong đợi: ['a', 'b', 'c', 'd']

Câu 2 (Lập trình hướng đối tượng - OOP): Kế thừa Hình học 
    Yêu cầu: Định nghĩa lớp cơ sở HinhChuNhat (Rectangle) và lớp con HinhVuong (Square) để thực hành tính toán diện tích và kế thừa.
        1. Lớp cơ sở HinhChuNhat (Rectangle)
            Thuộc tính: chieu_dai (float), chieu_rong (float).
            Phương thức khởi tạo __init__: Nhận chieu_dai và chieu_rong để khởi tạo.
            Phương thức tinh_dien_tich():
            Mục đích: Tính và trả về diện tích.
            Cách hoạt động: Diện tích = chieu_dai * chieu_rong.
            Giá trị trả về: Diện tích (float).
        2. Lớp con HinhVuong (Square)Kế thừa: Kế thừa từ HinhChuNhat.
            Phương thức khởi tạo __init__:
            Mục đích: Khởi tạo HinhVuong chỉ với một tham số canh (float).
            Cách hoạt động: Gọi phương thức khởi tạo của lớp cha (HinhChuNhat.__init__ hoặc super().__init__) và truyền giá trị canh cho cả chiều dài và chiều rộng.
'''

# Câu 1
def find_unique(anyList: list):
    outputList = []
    for i in anyList:
        if i not in outputList:
            outputList.append(i)
    return outputList

print(find_unique(['a', 'b', 'c', 'a', 'd', 'b']))
