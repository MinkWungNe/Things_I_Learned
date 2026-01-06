'''
1. Từ từ điển đến danh sách các danh sách và ngược lại! Cho từ điển sau:
cars = {"sports car":4, "convertible":5, "limousine":2}
    a. Chuyển đổi từ điển thành danh sách các danh sách.
(Kết quả mong đợi:[['sports car', 4], ['convertible', 5], ['limousine', 2]]).
    b. Chuyển đổi danh sách các danh sách trở lại từ điển ban đầu.
'''
dictionary = {"sports car": 4, "convertible": 5, "limousine": 2}
print(dictionary)
# a. Convert dictionary to list list
lst = []
for key, value in dictionary.items():
    lst.append([key, value])
    
print(lst)

# b. Convert list list back to dicrionary
dict2 = {}
for item in lst:
    dict2.update({item[0]:item[1]})
    
print(dict2)