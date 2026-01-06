'''
2. Mua một chiếc ô tô điện. Bạn muốn mua một chiếc ô tô điện mới, và đây là những chiếc xe bạn thích:
    • Model E-Nature, mức tiêu thụ năng lượng: 15 kWh trên 100 km, dung lượng pin: 75 kWh;
    • Model E-Green, mức tiêu thụ năng lượng: 18 kWh trên 100 km, dung lượng pin: 40 kWh.
Bạn muốn tính toán xem dung lượng pin của những chiếc xe này có đủ cho một chuyến đi dài 300 km hay không.
Để làm như vậy, bạn tạo:
    • Một lớp cha có tên là Vehicle. Hàm khởi tạo của nó chứa các thuộc tính biểu diễn model và mức tiêu thụ năng lượng.
    Phương pháp này tính toán năng lượng cần thiết bằng cách lấy mức tiêu thụ năng lượng chia cho 100 và nhân với quãng đường lái xe.
    • Một lớp con tên là ElectricCar. Lớp này thêm một thuộc tính biểu thị dung lượng pin và
    một phương thức in ra liệu chuyến đi có thể hoàn thành với năng lượng đã tính toán haykhông.
Bạn sẽ mua xe nào?
'''

class Vehicle:
    
    def __init__(self, model = "", batteryUsage: int = 0):
        self.__model = model
        self.__batUsage = batteryUsage
        
    def calculate_batUsage(self, distance):
        return (self.__batUsage / 100) * distance
    
class ElectricCar(Vehicle):
    def __init__(self, model = "", batteryUsage: int = 0, batteryCap = 0):
        super().__init__( model, batteryUsage)
        self.__batCap = batteryCap
        
    def canReach(self, distance):
        usage = self.calculate_batUsage(distance)
        if usage > self.__batCap:
            print("This car WILL NOT make it to the destination.")
        else:
            print('This car WILL make it to the destination.')
        
        print('Battery Capacity:', self.__batCap)
        print('Battery Usage:', usage)
        
# ===== TEST =====
car1 = ElectricCar('Model E-Nature', 15, 75)
car2 = ElectricCar('Model E-Green', 18, 40)

car1.canReach(300)
car2.canReach(300)