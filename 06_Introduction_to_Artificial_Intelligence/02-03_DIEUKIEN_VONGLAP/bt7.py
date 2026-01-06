ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

if nam < 0 or thang < 1 or thang > 12 or ngay < 1 or ngay > 31:
    print("Ngày, tháng, năm không hợp lệ!")
else:
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        so_ngay_trong_thang = 31
    elif thang in [4, 6, 9, 11]:
        so_ngay_trong_thang = 30
    else:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            so_ngay_trong_thang = 29
        else:
            so_ngay_trong_thang = 28
    if ngay < so_ngay_trong_thang:
        ngay += 1
    else:
        ngay = 1 
        if thang == 12:
            thang = 1
            nam += 1
        else:
            thang += 1  
    print(f"Ngày kế tiếp là: {ngay}/{thang}/{nam}")

# Here I learned about nested conditions and date validation in Python.