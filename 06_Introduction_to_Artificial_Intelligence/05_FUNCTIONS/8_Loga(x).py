'''
Viết chương trình tính logax với a, x là các số thực nhập vào từ bàn phím, và x>0, a>0, a != 1.( dùng logax=lnx/lna)

Write a program to calculate loga(x) with a, x are real numbers entered from the keyboard, and x>0, a>0, a != 1. (use loga(x)=ln(x)/ln(a))
'''
import math
def loga(a, x):
    if a <= 0 or a == 1 or x <= 0:
        return "Invalid input: a must be > 0 and != 1, x must be > 0"
    return math.log(x) / math.log(a)

a = float(input("Enter a (a > 0 and a != 1): "))
x = float(input("Enter x (x > 0): "))
result = loga(a, x)
print(f"log_{a}({x}) = {result}")