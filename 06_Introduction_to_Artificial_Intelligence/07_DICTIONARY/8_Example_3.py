'''
4. Các số trong một hình tam giác! Yêu cầu người chơi nhập một số nguyên. Sau đó, in ra
một hình tam giác, trong đó mỗi hàng chứa một số nguyên liên tiếp từ 1 đến số do người
chơi nhập vào. Ngoài ra, mỗi hàng nên bao gồm một danh sách chứa số từ hàng đó được 
lặp lại với số lần bằng chính số đó. Để làm được điều này, hãy sử dụng từ điển và cho
phép người chơi chơi bao lâu tùy thích!
(Ví dụ: đầu vào: 5.
Đầu ra dự kiến:
1 [1]
2 [2, 2]
3 [3, 3, 3]
4 [4, 4, 4, 4]
5 [5, 5, 5, 5, 5])
'''

while True:
    num = int(input('Insert number: '))
    lst = []

    for i in range(num):
        print(i + 1, end = ' ')
        for j in range(i + 1):
            lst.append(i + 1)
        print(lst)
        lst = []
    
    again = input('Do again? (Y/N)')
    
    if again.lower() == 'n':
        break
    print()