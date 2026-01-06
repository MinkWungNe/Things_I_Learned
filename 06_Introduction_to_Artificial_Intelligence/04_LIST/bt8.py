# Viết chương trình nhập vào một dãy n số thực M[0], M[1],..., M[n-1], sắp xếp dãy số theo thứ tự giảm dần. Xuất ra dãy số sau khi sắp xếp.
from random import randrange
print("Chương trình xử lý List")
n=int(input("Nhập số phần tử: "))
lst=[0]*n
for i in range(n):
    lst[i]= int(input(f"Nhập phần tử thứ {i}: "))

print("List ban đầu là:", lst)
lst.sort(reverse=True)
print("List sau khi sắp xếp giảm dần là:", lst)
