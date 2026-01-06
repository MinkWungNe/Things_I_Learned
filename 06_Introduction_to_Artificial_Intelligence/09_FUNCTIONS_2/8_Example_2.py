'''
2. Hiển thị các chữ cái đã đoán. 
Tạo một hàm vệ tinh cho một từ và một chữ cái đã đoán, hiển thị từ với chữ cái đã đoán được hiển thị đúng vị trí, trong khi các chữ cái còn lại,chưa đoán được, được hiển thị dưới dạng dấu gạch dưới.
(Ví dụ: đầu vào: ("l", "hello"). Ví dụ: đầu ra: _ _ l l _).
'''

def guess(charInput: chr, wordInput: str):
    string = []
    for char in wordInput:
        if char == charInput:
            string.append(char)
        else:
            string.append('_')

    return ' '.join(string)

print(guess('l', 'Hello'))