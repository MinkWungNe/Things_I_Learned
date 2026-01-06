'''
    Nhập toạ độ 2 điểm A(xA,yA), B(xB,yB). Tính và xuất độ dài đoạn AB. 
    Công thức: AB = sqrt((xB - xA)^2 + (yB - yA)^2)

    Input 2 points A and B coordinates. Calculate and print the length of line segment AB.
    Formula: AB = sqrt((xB - xA)^2 + (yB - yA)^2)
'''

from math import sqrt

def calculate_line_length(xA, yA, xB, yB):
    length = sqrt((xB - xA)**2 + (yB - yA)**2)
    return length

xA = float(input("Enter xA: "))
yA = float(input("Enter yA: "))
xB = float(input("Enter xB: "))
yB = float(input("Enter yB: "))
line_length = calculate_line_length(xA, yA, xB, yB)
print(f"The length of line segment AB is: {line_length}")
