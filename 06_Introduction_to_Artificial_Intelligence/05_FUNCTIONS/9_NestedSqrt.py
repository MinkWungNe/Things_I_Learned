'''
Viết chương trình tính căn bậc hai lồng nhau: sqrt(a + sqrt(a + sqrt(a + ...))) với a là số thực nhập vào từ bàn phím, a >= 0.

Write a program to calculate the nested square root: sqrt(a + sqrt(a + sqrt(a + ...))) with a being a real number entered from the keyboard, a >= 0.
'''
import math
def nested_sqrt(a):
    if a < 0:
        return "Invalid input: a must be >= 0"
    return (1 + math.sqrt(1 + 4 * a)) / 2
a = float(input("Enter a (a >= 0): "))
result = nested_sqrt(a)
print(f"The result of the nested square root is: {result}")