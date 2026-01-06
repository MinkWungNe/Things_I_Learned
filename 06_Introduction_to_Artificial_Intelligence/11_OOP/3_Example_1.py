'''
1. Thêm sản phẩm trong cửa hàng trực tuyến! Tạo thêm hai đối tượng từ lớp Product với các đặc điểm sau:
    a. Một quả bóng bãi biển tên là Giant ball, giá gốc: 10 xu, giảm giá khi ra mắt: 0,50 xu.
    Tính giá của nó trước và sau khi áp dụng phiếu giảm giá SAVE4.
    b. Một cuốn nhật ký có tên My adventures, giá 15 xu, giảm giá khi ra mắt: 3 xu. Tính giá
    của nó trước và sau khi áp dụng phiếu giảm giá SPRINGSALES30.
    
Bạn sẽ nhận được gì khi in từng đối tượng?
'''

class Product:
    def __init__(self, name):
        self.name = name
        self.price =0 
        self.discount = 0
        
    def apply_coupon(self, coupon):
        if coupon == 'SAVE4':
            self.discount += 4
            print('Coupon SAVE4 ĐƯỢC ÁP DỤNG')
        elif coupon == 'SUMMER10':
            self.discount += 10
            print('Coupon SUMMER10 ĐƯỢC ÁP DỤNG')
        else:
            print('Coupon của bạn KHÔNG HỢP LỆ')
            
    def calculate_price(self):
        updated_price = self.price - self.discount
        return updated_price
    
    def __str__(self):
        return 'Name: ' + self.name

# a. Make a ball 'Giant ball' | original price = 10 | discount = 0.5  THEN apply 'SAVE4' coupon
ball = Product('Giant ball')
ball.price = 10
ball.discount = 0.50

before = ball.calculate_price()
ball.apply_coupon('SAVE4')
after = ball.calculate_price()

print('Name:', ball.name, '| Price BEFORE:', before, '| Price AFTER:', after)

# b. Make a Diary 'My adventures' | original price = 15 | discount = 3 THEN apply 'SPRINGSALES30' coupon
diary = Product('My adventures')
diary.price = 15
diary.discount = 3

before = diary.calculate_price()
diary.apply_coupon('SPRINGSALES30')
after = diary.calculate_price()

print('Name:', diary.name, '| Price BEFORE:', before, '| Price AFTER:', after)