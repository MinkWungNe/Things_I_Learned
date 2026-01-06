'''
1. Đặt đồ ăn trực tuyến. Bạn phải tạo một chương trình phần mềm mới cho việc đặt đồ ăn trực tuyến. Khách hàng yêu cầu 
một hệ thống đặt hàng cơ bản với hai tùy chọn tùy chỉnh, một cho pizza và một cho burger. Đơn hàng cơ bản có giá ban đầu 
là 10 xu. Đối với pizza, giá tăng 20% nếu kích thước là cỡ vừa, và tăng 50% nếu kích thước là cỡ lớn. Đối với burger, 
giá tăng 1,5 xu nếu khách hàng thêm phô mai và tăng 1 xu nếu họ thêm hành tây. Để kiểm tra mã của bạn, hãy tạo bốn đơn hàng
một pizza nhỏ, một pizza cỡ vừa, và một pizza cỡ lớn, cũng như một burger có thêm phô mai và hành tây. Tổng chi phí là bao nhiêu?
'''

BASE_PRICE = 10  # xu

# ----- SupperClass -----
class FoodOrder:
    def __init__(self, base_price=BASE_PRICE):
        self.base_price = base_price

    def calculate_price(self):
        """Phương thức sẽ được ghi đè ở lớp con"""
        return self.base_price


# ----- Pizza class -----
class Pizza(FoodOrder):
    def __init__(self, size):
        super().__init__()
        self.size = size.lower()

    def calculate_price(self):
        if self.size == "small":
            return self.base_price
        elif self.size == "medium":
            return self.base_price * 1.2
        elif self.size == "large":
            return self.base_price * 1.5
        else:
            raise ValueError("Kích cỡ pizza không hợp lệ!")


# ----- Burger class -----
class Burger(FoodOrder):
    def __init__(self, cheese=False, onion=False):
        super().__init__()
        self.cheese = cheese
        self.onion = onion

    def calculate_price(self):
        price = self.base_price
        if self.cheese:
            price += 1.5
        if self.onion:
            price += 1
        return price

#===== TEST =====
# ----- Make orders -----
pizza_small = Pizza("small")
pizza_medium = Pizza("medium")
pizza_large = Pizza("large")
burger_full = Burger(cheese=True, onion=True)

# ----- Total -----
orders = [pizza_small, pizza_medium, pizza_large, burger_full]
total = sum(order.calculate_price() for order in orders)

# ----- Result -----
print("Chi tiết đơn hàng:")
print(f"Pizza nhỏ: {pizza_small.calculate_price()} xu")
print(f"Pizza vừa: {pizza_medium.calculate_price()} xu")
print(f"Pizza lớn: {pizza_large.calculate_price()} xu")
print(f"Burger (phô mai + hành tây): {burger_full.calculate_price()} xu")
print(f"Tổng chi phí: {total} xu")
