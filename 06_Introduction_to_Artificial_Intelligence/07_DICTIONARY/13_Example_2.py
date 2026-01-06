'''
2. Trò chơi bảng cửu chương! Bạn là một lập trình viên tại một công ty trò chơi giáo dục.
Nhiệm vụ của bạn là tạo một trò chơi trong đó trẻ em nhập một số và bạn sẽ hiển thị bảng
cửu chương tương ứng. Để triển khai trò chơi, hãy tạo một từ điển trong đó các khóa là
các số từ 1 đến 10 và các giá trị là kết quả của phép nhân giữa khóa và giá trị do trẻ nhập.
Sử dụng vòng lặp for và cho phép trẻ chơi bao lâu tùy thích.
(Ví dụ đầu vào: 4
Ví dụ đầu ra:
1 x 4 = 4
2 x 4 = 8
3 x 4 = 12
4 x 4 = 16
5 x 4 = 20
6 x 4 = 24
7 x 4 = 28
8 x 4 = 32
9 x 4 = 36
10 x 4 = 40).
'''
while True:
    n = int(input('Chose number to multiply: '))  # take input
    MultiplyDict = {}
    # calculate the multiply numbers
    for i in range(1,11):   
        MultiplyDict[i] = i * n

    # print result
    for key, value in MultiplyDict.items():
        print(key, "x", n, "=", value)

    # ask for retry
    result = input('Again? (Y/N) ')
    if result.lower() == 'n':
        print('Bye!')
        break