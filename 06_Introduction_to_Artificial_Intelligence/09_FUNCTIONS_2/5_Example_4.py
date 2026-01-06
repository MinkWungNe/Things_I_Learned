'''
4. Nhân đôi số. Viết một hàm yêu cầu người dùng nhập một số và in ra một từ điển trong
đó các khóa là các số có giá trị nhỏ hơn số đầu vào, và các giá trị là số kép của mỗi khóa.
Lưu ý rằng hàm không nhận bất kỳ đối số nào. Hàm input() để yêu cầu nhập số nằm bên trong hàm.
(Ví dụ: người dùng nhập: 5
Kết quả mong đợi: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10})
'''

def print_DoubledDictionary(num: int):
    dictionary = {}
    for i in range(num):
        dictionary.update({i+1:(i+1)*2})
        
    print(dictionary)
print_DoubledDictionary(int(input('Enter an Integer: ')))