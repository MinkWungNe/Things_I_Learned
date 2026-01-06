thang = int(input("Nhập tháng (1-12): "))
if thang < 1 or thang > 12:
    print("Tháng không hợp lệ! Vui lòng nhập tháng từ 1 đến 12.")
elif thang in [1, 2, 3]:
    print(f"Tháng {thang} thuộc Quý 1.")
elif thang in [4, 5, 6]:
    print(f"Tháng {thang} thuộc Quý 2.")
elif thang in [7, 8, 9]:
    print(f"Tháng {thang} thuộc Quý 3.")
else:
    print(f"Tháng {thang} thuộc Quý 4.")