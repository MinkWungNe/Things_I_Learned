'''
Câu 1: Thực hành hàm cơ bản trong Python
Viết các hàm Python sau và chạy thử trong chương trình chính (main()):
    (a)  Viết hàm is_prime(n) kiểm tra số nguyên dương n có phải là số nguyên tố không.
    → In ra danh sách các số nguyên tố từ 1 đến 50.
    (b) Viết hàm count_vowels(s) đếm số nguyên âm trong chuỗi s.
    → Gọi hàm và in ra kết quả với chuỗi: "Artificial Intelligence"
    (c) Viết hàm average(numbers) nhận vào danh sách số và trả về giá trị trung bình.
    → Gọi hàm với danh sách [4, 7, 2, 9, 5] và in kết quả.
'''

# a. Write prime function   - Prime Number: only diviable by 1 and itself
def is_Prime(n):
    dem=0
    for i in range(1,n+1):
        if n % i ==0:
            dem+=1
    return dem == 2

PrimeList = []
for i in range(50):
    if is_Prime(i):
        PrimeList.append(i)
        
print(PrimeList)

# b. Write count vowels
def count_vowels(s):
    vowels = ['a', 'ă', 'â', 'e', 'ê', 'i', 'o', 'ô', 'ơ', 'u', 'ư', 'y']
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    
    return count

print(count_vowels("Tôi Tên Tân"))

# c. Write average function
def average(numList):
    sum = 0
    size = len(numList)
    for num in numList:
        sum += num
    return sum/size

print(average([4,7,2,9,5]))



