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
    def apply_coupon(self,coupon):
        if coupon == "SAVE4":
            self.__discount += 4
            print('Apllied "SAVE4" coupon!')
        elif coupon == "SUMMER10":
            self.__discount += 10
            print('Apllied "SUMMER10" coupon!')
        else: 
            print('No coupon applied.')
            
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
    
t_shirt = Product("Feel Good")
print("T-Shirt name:", t_shirt.name)

print('===== Origin Price =====')
t_shirt.set_price(30)
print('Price:', t_shirt.get_price())

print('===== Set Discount =====')
t_shirt.set_discount(4)
print('Discount:', t_shirt.get_discount())

print('===== Final Price =====')
price = t_shirt.calculate_price()
print('Price:', price)

print('===== Price After Coupon =====')
t_shirt.apply_coupon('SAVE4')
price = t_shirt.calculate_price()
print('Price:', price)