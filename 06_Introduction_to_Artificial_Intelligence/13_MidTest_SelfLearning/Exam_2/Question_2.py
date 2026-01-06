'''
Đề 2 Luyện Tập Python
Câu 1 (Vấn đề chung): Đếm Tần suất Từ Đơn giản 📑
    Yêu cầu: Viết một hàm Python có tên là dem_tan_suat_tu(van_ban) nhận vào một chuỗi văn bản. Hàm phải trả về một dictionary, trong đó key là các từ duy nhất trong văn bản (chuyển sang chữ thường), và value là số lần từ đó xuất hiện.

    Ví dụ (Input/Output):
    Input: "Python là ngôn ngữ lập trình. Python rất mạnh mẽ."
    Output mong đợi: {'python': 2, 'là': 1, 'ngôn': 1, 'ngữ': 1, 'lập': 1, 'trình.': 1, 'rất': 1, 'mạnh': 1, 'mẽ.': 1}

Câu 2 (Lập trình hướng đối tượng - OOP): Kế thừa trong Quản lý Kho 📦
    Yêu cầu: Định nghĩa một lớp cơ sở KhoHang và một lớp con KhoThucPham.
    1. Lớp cơ sở KhoHang (Base Class)
        Thuộc tính: danh_sach_san_pham (list, khởi tạo là một list rỗng).
        Phương thức them_san_pham(san_pham):
        Mục đích: Thêm một mục hàng hóa (dưới dạng chuỗi) vào danh sách kho hàng.
        Tham số: self, san_pham (string).

    2. Lớp con KhoThucPham (Derived Class)
        Kế thừa: Kế thừa từ KhoHang.
        Phương thức kiem_tra_gan_nhat():
        Mục đích: Mô phỏng thao tác kiểm tra kho (sử dụng kế thừa).
        Cách hoạt động: In ra thông báo cố định: "Đã kiểm tra kho thực phẩm vào hôm nay."
'''

# Câu 2:
class KhoHang:
    def __init__(self, productList = []):
        self.list = productList

    def addProduct(self, product: str):
        if product not in self.list:
            self.list.append(product)

class KhoThucPham(KhoHang):
    def __init__(self, productList = []):
        super().__init__(productList)
    
    def checkProduct(self):
        print('Đã kiểm tra kho thực phẩm vào hôm nay.')

# TEST
kho = KhoThucPham()
kho.addProduct('Banana')
kho.checkProduct()