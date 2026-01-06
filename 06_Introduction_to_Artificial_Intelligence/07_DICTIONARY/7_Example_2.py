'''
2. Dịch chuyển các phần tử danh sách! Cho từ điển sau:
dictionary = {"numbers":[2,3,4,5,6,7,8,9,10]}
    a. Thêm một cặp khóa:giá trị, trong đó khóa là chuỗi chẵn và giá trị là một danh sách
chứa True cho các số chẵn và False cho các số lẻ.
(Kết quả mong đợi:
{"numbers": [2, 3, 4, 5, 6, 7, 8, 9, 10],
 "even": [True, False, True, False, True, False, True, False, True]}).
    b. Trừ 1 cho mỗi số.
    c. Làm thế nào để sửa đổi danh sách Boolean sao cho nó tương ứng với danh sách số
mới? Gợi ý: Chỉ cần dịch chuyển nó!
'''

dictionary = {"numbers":[2,3,4,5,6,7,8,9,10]}

lst = []
# a. Add a key determine the number even or odd
for num in dictionary["numbers"]:
    if num % 2 == 0:
        lst.append(True)
    else:
        lst.append(False)
dictionary.update({"even": lst})

# b. minus 1 for every num
index = 0
for num in dictionary["numbers"]:
    dictionary["numbers"][index] = num - 1
    index += 1

# c. since the numbers changed, update the even
index = 0
for num in dictionary["even"]:
    dictionary["even"][index] = not dictionary["even"][index]
    index += 1

print('THE FINAL RESULT--------------------------------')
for key in dictionary.keys():
    print(dictionary[key])