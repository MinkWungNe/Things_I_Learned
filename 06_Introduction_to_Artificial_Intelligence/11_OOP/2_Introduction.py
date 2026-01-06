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
    
    
# TEST 1
t_shirt = Product("Feel good")
t_shirt.price = 30
t_shirt.discount = 4
print('Name:', t_shirt.name, '| Origin Price:', t_shirt.price, '| Discount:', t_shirt.discount)

t_shirt_price = t_shirt.calculate_price()
print('Price after discount:', t_shirt_price)

t_shirt.apply_coupon('SAVE4')
t_shirt_price = t_shirt.calculate_price()
print('Price after added coupon "SAVE4":', t_shirt_price, '\n')

print('------------------------------------------------------------')

# TEST 2
lamp = Product('Lux')
lamp.price = 40

print('Name:', lamp.name, '| Origin Price:', lamp.price, '| Discount:', lamp.discount)

lamp.apply_coupon('SUMMER10')
lamp.price = lamp.calculate_price()
print('Price after applied coupon "SUMMER10":', lamp.price)