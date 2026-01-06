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

# Câu 1
name = input('Name (Vietnamese form): ').split()
year = int(input('Year of birth: '))

## Process String
surname = name[0]
firstname = name[len(name) - 1]
middlename = ""

for namePart in name:
    if name.index(namePart) == 0 or name.index(namePart) == len(name) - 1:
        continue
    middlename += namePart + ' '

## Reformat surname and middlename
restName = surname[0]
for middleNamePart in middlename.split():
    restName += "." + middleNamePart[0]

## Process Year of birth
cur_year = 2025

age = cur_year - year

## OUTPUT
print('FirstName: {:s}\nSurname&LastName: {:s}\nAge: {:.0f}'.format(firstname, restName, age))
