'''
    Viết hàm tính tổng ước số để áp dụng chung cho 2 bài dưới đây:
a)	Kiểm tra số nguyên dương n có phải là  số hoàn thiện (Pefect number) hay không? (Số hoàn thiện là số có tổng các ước số của nó (không kể nó) thì bằng chính nó. Vd: 6 có các ước số là 1,2,3 và 6=1+2+3 6 là số hoàn thiện)
b)	Kiểm tra số nguyên dương n có phải là  số thịnh vượng (Abundant number)hay không? (Số thịnh vượng là số có tổng các ước số của nó (không kể nó) thì lớn hơn nó. Vd:12 có các ước số là 1,2,3,4,6 và 12<1+2+3+4+6 12 là số thịnh vượng)
--------------------------------------------------------------------------------------
    Write a function to calculate the sum of divisors to apply to the following two problems:
a)	Check if a positive integer n is a Perfect number or not? (A Perfect number is a number whose sum of its divisors (excluding itself) equals the number itself. For example: 6 has divisors 1, 2, 3 and 6=1+2+3 6 is a Perfect number)
b)	Check if a positive integer n is an Abundant number or not? (An Abundant number is a number whose sum of its divisors (excluding itself) is greater than the number itself. For example: 12 has divisors 1, 2, 3, 4, 6 and 12<1+2+3+4+6 12 is an Abundant number)
'''
import math

def tinh_tong_uoc_so(n):
    """
    Hàm này tính tổng các ước số thực sự của một số nguyên dương n.
    Ước số thực sự là các ước số nhỏ hơn n.
    """
    # Số 1 không có ước số thực sự nào nhỏ hơn nó
    if n <= 1:
        return 0
    
    # Bắt đầu tổng với 1 vì 1 luôn là ước của mọi số
    tong_uoc = 1
    
    # Duyệt từ 2 đến căn bậc hai của n để tìm các cặp ước số
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            # Nếu i là ước số, cộng i vào tổng
            tong_uoc += i
            
            # Cộng cả cặp ước số của nó (n/i)
            # Tránh cộng hai lần nếu n là số chính phương (ví dụ 36 có cặp ước 6*6)
            if i * i != n:
                tong_uoc += n // i
                
    return tong_uoc

def kiem_tra_so_hoan_thien(n):
    """
    Kiểm tra xem n có phải là số hoàn thiện hay không.
    Số hoàn thiện có tổng các ước số thực sự bằng chính nó.
    Ví dụ: 6 = 1 + 2 + 3
    """
    tong_uoc = tinh_tong_uoc_so(n)
    return tong_uoc == n

def kiem_tra_so_thinh_vuong(n):
    """
    Kiểm tra xem n có phải là số thịnh vượng hay không.
    Số thịnh vượng có tổng các ước số thực sự lớn hơn chính nó.
    Ví dụ: 12 < 1 + 2 + 3 + 4 + 6 = 16
    """
    tong_uoc = tinh_tong_uoc_so(n)
    return tong_uoc > n

# --- Phần chính của chương trình ---
if __name__ == "__main__":
    while True:
        try:
            # Yêu cầu người dùng nhập số
            so_n = int(input("Nhập một số nguyên dương n để kiểm tra: "))
            if so_n > 0:
                break
            else:
                print("Vui lòng nhập một số NGUYÊN DƯƠNG lớn hơn 0.")
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")

    print(f"\n--- Kết quả kiểm tra cho số {so_n} ---")
    
    # a) Kiểm tra số hoàn thiện
    if kiem_tra_so_hoan_thien(so_n):
        print(f"{so_n} là một số hoàn thiện (Perfect number).")
    else:
        print(f"{so_n} không phải là số hoàn thiện.")
        
    # b) Kiểm tra số thịnh vượng
    if kiem_tra_so_thinh_vuong(so_n):
        print(f"{so_n} là một số thịnh vượng (Abundant number).")
    else:
        print(f"{so_n} không phải là số thịnh vượng.")