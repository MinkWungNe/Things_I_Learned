'''
1. Cửa hàng nội thất. Bạn là quản lý của một cửa hàng nội thất. Dưới đây là các món đồ
nội thất đang được lưu trữ:
store = {"furniture": ["chair", "table", "sofa"], "amount": [24, 7, 6], "price": [200, 500, 1200]}
    a. Một khách hàng mới đến và mua 4 chiếc ghế. Hãy cập nhật từ điển bằng một phép toán số học.
    b. Sau vài ngày, bạn nhận được những món đồ nội thất mới: 9 tấm thảm, mỗi tấm trị giá 150 đô la và 4 chiếc đèn, mỗi chiếc trị giá 180 đô la. Vì vậy, bạn thêm chúng vào từ điển 
    (sử dụng các cú pháp khác nhau).
    c. Chủ một nhà hàng đến cửa hàng của bạn và mua tất cả các bàn. Hãy cập nhật từ điển (sử dụng ít nhất 2 cú pháp khác nhau).
    d. Để hình dung rõ hơn những gì còn lại, bạn in từ điển bằng cách căn chỉnh các khóa sang phải và các giá trị sang trái.
    e. Tổng giá của đồ nội thất trong kho là bao nhiêu?
'''

store = {"furniture": ["chair", "table", "sofa"],
         "amount": [24, 7, 6],
         "price": [200, 500, 1200]}

# a. A customer bough 4 chairs. Update the amount
index = 0
for furniture in store["furniture"]:
    if furniture == 'chair':
        break
    index += 1
store['amount'][index] -= 4

# b. Add new items: 9 carpets, each 150$. 4 lamps, each 180$.
store["furniture"] += ['carpet', 'lamp']
store["amount"] += [9, 4]
store["price"] += [150, 180]

# c. A customer bought all table. Update the store
for furniture in store["furniture"]:
    if furniture == 'table':
        break
    index += 1
del store["furniture"][index]
del store["amount"][index]
del store["price"][index]
print(store)

# d. Fancy print the data, with key on the left and value on the right
index = 0
for furniture in store["furniture"]:
    print(furniture, '\t', store["amount"][index])
    index += 1

# e. Calculate sum vavlue of the whole store.
index = 0; sum = 0
for amount in store["amount"]:
    sum += amount * store["price"][index]
    index += 1
    
print('SUM:', sum)