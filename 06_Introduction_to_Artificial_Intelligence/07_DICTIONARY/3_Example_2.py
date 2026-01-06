'''
2. Tại một phòng khám thú y. Bạn là bác sĩ thú y tại một phòng khám thú y, và đây là một
số thú cưng bạn hiện đang chăm sóc.
pets = [{"name":"Toby", "animal type":"dog", "age":2},
{"name":"Kitty", "animal type":"cat", "age":5},
{"name":"Tiki", "animal type":"parrot", "age":1}]
    a. Bạn vừa tiếp nhận một bệnh nhân mới, một chú ngựa 4 tuổi tên là Sugar, và bạn thêmnó vào danh sách.
Nhập môn Trí tuệ nhân tạo – Lập trình Python
    b. Bây giờ, bạn cần in ra tất cả tên các loài động vật. Trước tiên, hãy thực hiện việc này
bằng vòng lặp for qua các phần tử và sau đó bằng vòng lặp for qua các chỉ mục.
    c. Cuối cùng, bạn thêm một mục cho biết tất cả các loài động vật hiện đang ở phòng
khám (bạn sử dụng kiểu dữ liệu nào?).
'''
pets = [{'name': 'Toby', 'animal type': 'dog', 'age': 2},
        {'name': 'Kitty', "animal type": "cat", "age": 5},
        {"name": "Tiki", "animal type": "parrot", "age": 1}]
print('Pets Initialized: --------------------------------------------------------')
print(pets)

# a. Add new pet: 4.yo Horse named 'Sugar'
pets.append({'name': 'Sugar', 'animal type': 'horse', 'age': 4})
print('Pets after ADDED new pet: ------------------------------------------------')
print(pets)

# b. Fancy print the pets list
for pet in pets:
    for key in pet:
        print(key, ':', pet[key])
    print()
    
# c. Add an attribute 'isAtVet'
for pet in pets:
    pet['isInVet'] = True
    
print('Pets after ADDED isInVet: -----------------------------------------------')
for pet in pets:    # I used fancy print for better visibilities
    for key in pet:
        print(key, ':', pet[key])
    print()