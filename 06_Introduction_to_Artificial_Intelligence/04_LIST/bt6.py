from random import randint

n = int(input("Nhập số phần tử của list: "))
a = [randint(1, 100) for _ in range(n)]
print("List a:", a)