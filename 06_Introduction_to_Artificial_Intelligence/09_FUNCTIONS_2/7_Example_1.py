'''
1. Chọn một từ ngẫu nhiên. Tạo một hàm vệ tinh cho một danh sách các từ, 
trả về một từđược chọn ngẫu nhiên ở dạng chữ thường.
(Ví dụ: đầu vào: ["muỗng", "Nĩa", "DAO"]. Ví dụ: đầu ra: "nĩa").
'''
from random import randrange

def choose(set):
    rand = randrange(0, len(set))

    return set[rand].lower()

# TEST
set = ['Coconut', 'Jean', 'OK']

result = choose(set)
print(result)