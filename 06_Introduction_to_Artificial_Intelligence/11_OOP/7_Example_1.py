'''
1. Kiểm thử lớp cha. Khởi tạo một đối tượng t_shirt từ lớp cha Product có các đặc điểm
giống như trong chương trước, tức là tên: Feel good, giá khởi điểm: 30 xu, giảm giá khi
ra mắt: 4 xu, phiếu giảm giá SAVE4. Hãy thử thiết lập một mẫu sách và gọi phương thức
read_sample(). Điều gì xảy ra và tại sao?
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

class Book(Product):
    
    def __init__(self, name):
        super().__init__(name)
        self.__book_sample = ""
        
    # ==== GETTER / SETTER ====
    def get_book_sample(self, name):
        if isinstance(name, str):
            self.__book_sample = name
        else:
            raise TypeError("Book's name have to be a String")
    
    def set_book_sample(self, name):
        if isinstance(name,str):
            self.__book_sample = name    
    
    def read_sample(self):
        if self.__book_sample != "":
            print(self.__book_sample + "[...] Đã có chưa? Mua đi!")
        else:
            print('Book không tồn tại.')
            
# ==== TEST ====
t_shirt = Product("Feel Good")
print("T-Shirt name:", t_shirt.name)

print('===== Origin Price =====')
t_shirt.set_price(30)
print('Price:', t_shirt.get_price())

print('===== Set Discount =====')
t_shirt.set_discount(4)
print('Discount:', t_shirt.get_discount())

print('===== Price After Coupon =====')
t_shirt.apply_coupon('SAVE4')
price = t_shirt.calculate_price()
print('Price:', price)

t_shirt.set_book_sample() # Expects Error

# -> When try calling a subclass's method from supperclass, the supperclass know nothing about that.