'''
Bạn vừa tổ chức một bữa tiệc và muốn gửi thiệp Thank you đến những người đã tham
dự. Hãy tạo một hàm lấy tên làm đối số và in ra một thông điệp Thank you có chứa tên
của người tham dự (ví dụ: Thank you Maria):
'''

def print_thankyou(name):
    print('Thank you', name)
    
print_thankyou('Maria')
print_thankyou('Xiao')
print('----------------------------------------')
'''
Sau khi suy nghĩ kỹ, bạn quyết định in thiệp Thank you trang trọng sẽ phù hợp hơn. Sửa
đổi hàm trước đó để lấy ba đối số—tiền tố, tên và họ—và in một thông điệp cảm ơn chứa
chúng (ví dụ: Thank you Mrs Maria Lopez):
'''

def print_fancy_thankyou(prefix, lastname, firstname = ""): # default firstname is empty
    '''
    prefix: Mr. - Mrs.
    '''
    print('Thank you', prefix, lastname, firstname)
    
print_fancy_thankyou('Mrs', 'Maria', 'Lopez')
print_fancy_thankyou('Mr', 'Xiao', 'Li')
print('----------------------------------------')
'''
Cuối cùng, bạn nhận ra rằng tiền tố và/hoặc họ cũng bị thiếu đối với một số khách. Hãy
sửa đổi hàm cho phù hợp:
'''

def print_EvenMoreFancy_Thankyou(prefix = "", lastname = "", firstname = ""):
    print("Mr/Mrs:",prefix)
    print("LastName:", lastname)
    print('FirstName:', firstname)
    print('Thank you', prefix, lastname, firstname)

print_EvenMoreFancy_Thankyou("Mr", 'Maria', 'Lopez')
print_EvenMoreFancy_Thankyou(lastname = "Xiao", firstname = "Li")