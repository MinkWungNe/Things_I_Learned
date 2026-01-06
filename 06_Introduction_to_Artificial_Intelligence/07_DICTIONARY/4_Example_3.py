'''
3. Nước ép! Bạn sở hữu một quầy nước ép và cần theo dõi lượng nước ép và doanh số
bán hàng.
    a. Tạo một danh sách các từ điển chứa 3 hương vị nước ép (cam, chanh và lựu), giá cả và
màu sắc của chúng.
    b. Với mỗi loại nước ép, hãy thêm một mục mới có khóa là 'in shop' và giá trị là Boolean.
    c. Bạn vừa nhận được một đơn hàng mới (nước ép nho) và bạn thêm nó vào danh sách.
    d. Giá trung bình của một loại nước ép là bao nhiêu?
'''

# a. Create a dictionary for the juices
juices = [{"flavor": 'Orange', "Price": 20000, "Color": "Orange"},
          {"flavor": 'Lime', "Price": 10000, "Color": "Yellow"},
          {"flavor": 'Pomegranate', "Price": 25000, "Color": "Red"}]

print('Juices Initialized: -------------------------------------------------------')
print(juices)

# b. Add 'in shop' for every juices
for juice in juices:
    juice.update({'in shop': True})
    
print('Juices after ADDED \'in shop: ---------------------------------------------')
print(juices)

# c. Add Grape juice to dictionary
juices.append({'flavor': 'Grape', "Price": 23000, "Color": 'Purple'})
print('Juices after ADDED Grape: -------------------------------------------------')
print(juices)

# d. Average cost
cost = 0
count = 0
for juice in juices:
    cost += juice['Price']
    count += 1
cost /= count
print('Average Cost: -------------------------------------------------------------')
print(int(cost))
