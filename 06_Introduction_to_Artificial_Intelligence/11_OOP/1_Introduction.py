'''
Hãy bắt đầu từ điểm đầu tiên của bài tập. Ở đây, chúng ta có một lớp đại diện cho mẫu
trang web và một đối tượng đại diện cho chiếc áo phông—chúng ta sẽ tạo đối tượng đại
diện cho chiếc đèn ở cuối phần đầu tiên này. Hãy đọc đoạn mã bên dưới và cố gắng hiểu
cú pháp và chức năng của nó.
'''

class Product:
    
    # Constructor
    def __init__(self, name):
        self.name = name
        self.price = 0
        self.discount = 0
        
# TEST 1 
t_shirt = Product("Feel good")
print('Name:', t_shirt.name)
print('Price:', t_shirt.price)
print('Discount:', t_shirt.discount)

t_shirt.price = 30
t_shirt.discount = 4
print('Price:', t_shirt.price, 'NEW')
print('Discount:', t_shirt.discount, 'NEW')

# TEST 2
lamp = Product("Lux")
lamp.price = 40
print('Name:', lamp.name)
print('Price:', lamp.price)
print('Discount:', lamp.discount)