n = int(input("Nhập số phần tử: "))
lst = [0] * n
for i in range(n):
    lst[i] = int(input(f"Nhập phần tử thứ {i + 1}: "))

print("List ban đầu là:", lst)

# Danh sách gồm số lẻ và tổng bao nhiêu số lẻ
odd_numbers = [x for x in lst if x % 2 != 0]
sum_odd = sum(odd_numbers)
print("Các số lẻ trong list:", odd_numbers)
print("Tổng các số lẻ là:", sum_odd)

# Danh sách gồm số chẵn và tổng bao nhiêu số chẵn
even_numbers = [x for x in lst if x % 2 == 0]
sum_even = sum(even_numbers)
print("Các số chẵn trong list:", even_numbers)
print("Tổng các số chẵn là:", sum_even)

# Danh sách các số nguyên tố
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
prime_numbers = [x for x in lst if is_prime(x)]
print("Các số nguyên tố trong list:", prime_numbers)

# Danh sách không phải số nguyên tố
non_prime_numbers = [x for x in lst if not is_prime(x)]
print("Các số không phải nguyên tố trong list:", non_prime_numbers)

