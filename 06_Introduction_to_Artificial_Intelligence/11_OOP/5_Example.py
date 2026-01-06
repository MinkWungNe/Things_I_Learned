'''
1. Hãy thêm nhiều mặt hàng hơn vào cửa hàng trực tuyến! Từ lớp Product đã cập nhật, hãy khởi tạo các đối tượng sau từ chương trước:
    • Một chiếc đèn tên là Lux, giá gốc: 40 xu, không giảm giá khi ra mắt. Tính giá của nó trước và sau khi áp dụng phiếu giảm giá SUMMER10.
    • Một quả bóng bãi biển tên là Giant ball, giá gốc: 10 xu, giảm giá khi ra mắt: 0,50 xu. Tính giá của nó trước và sau khi áp dụng phiếu giảm giá SAVE4.
    • Một cuốn nhật ký tên là My adventures, giá 15 xu, giảm giá khi ra mắt: 3 xu. Tính giá của nó trước và sau khi áp dụng phiếu giảm giá SPRINGSALES30.
'''

class Product:
    
    #--- CONSTRUCTOR ---
    def __init__(self,name):
        self.name = name        # public attribute
        self.__price = 0        # use __<AttributeName> to set attribute to PRIVATE
        self.__discount = 0
        self.__tax_rate = 0.02
        
    #--- SETTER/GETTER ---
    def get_price(self):
        return self.__price
    
    def get_discount(self):
        return self.__discount
    
    def set_price(self, price):
        if isinstance(price, (int,float)) and price > 0:
            self.__price = price
        else:
            raise ValueError('Wrong input, price must be bigger then 0.')
        
    def set_discount(self, discount):
        if isinstance(discount, (int,float)) and 0 < discount < self.__price:
            self.__discount = discount
        else:
            raise ValueError('Wrong input, discount must bigger then 0 and smaller then Price.')
        
    #--- METHODS ---
    def apply_coupon(self,coupon, announce):
        isAnnounce = False
        if coupon == "SAVE4":
            self.__discount += 4
            isAnnounce = True
        elif coupon == "SUMMER10":
            self.__discount += 10
            isAnnounce = True
        
        if isAnnounce and announce:
            print('Coupon', coupon, 'applied!')
            
    def __calculate_tax(self, price):
        tax = round(price*self.__tax_rate, 2)
        print('Price:', price, '\t|\t Tax:', tax)
        return tax
    
    def calculate_price(self):
        discounted_price = self.__price - self.__discount
        
        tax = self.__calculate_tax(discounted_price)
        
        taxed_price = discounted_price + tax
        
        return taxed_price
    
    #--- BUILT-IN METHOD ---
    def __str__(self):
        return 'Name: ' + self.name
    

# ==== TEST ====
# a. Make a 'Lux' lamp with:  Price = 40 | Discount = 0 | Applies coupon 'SUMMER10'
lamp = Product('Lux')
lamp.set_price(40)

print('===== Lamp =====')
before = lamp.calculate_price()
print('Price bafore coupon:', before)

lamp.apply_coupon('SUMMER10', False)

after = lamp.calculate_price()
print('Price after coupon:', after)

# b. Make a 'Giant ball' ball with: Price = 10 | Discount = 0.5 | Applies coupon 'SAVE4'
ball = Product('Giant ball')
ball.set_price(10)
ball.set_discount(0.5)

print('===== Lamp =====')
before = ball.calculate_price()
print('Price bafore coupon:', before)

lamp.apply_coupon('SUMMER10', False)

after = ball.calculate_price()
print('Price after coupon:', after)

# c. Make a 'My Adventures' dairy with: Price = 15 | Discount = 3 | Apllies coupon 'SPRINGSALES30'
dairy = Product('My Adventures')
dairy.set_price(15)
dairy.set_discount(3)

print('===== Lamp =====')
before = dairy.calculate_price()
print('Price bafore coupon:', before)

lamp.apply_coupon('SPRINGSALES30', False)

after = dairy.calculate_price()
print('Price after coupon:', after)