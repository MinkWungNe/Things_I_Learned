'''
1. Thông tin sinh viên. Đối với tình huống sau, hãy tạo mã tương tự như mã được trình
bày trong chương này. Bạn làm việc tại Phòng Đăng ký của một trường học và đây là dữ
liệu của một sinh viên:
student = {"First name":"Bruce", "Last name":"Zhiang", "Sex":"Male", "Age":21,
"Course":"Literature", "Hobby":"Swimming"}
    a. In ra tất cả các khóa và giá trị của chúng.
    b. In ra tất cả các khóa.
    c. In ra tất cả các giá trị.
    d. Bruce gần đây đã chuyển khóa học của mình từ Literature to Foreign Languages, vì
vậy bạn cần cập nhật dữ liệu của anh ấy.
    e. Có hai thông tin bị thiếu: Address and Phone number,vì vậy bạn cần thêm chúng vào
(sử dụng (hai cú pháp khác nhau).
    f. Cuối cùng, do chính sách bảo mật mới, bạn phải xóa Sex và Hobby.
'''
student = {'First name': 'Bruce',
           'Last name': 'Zhiang',
           'Sex': 'Male',
           'Age': 21,
           'Course': 'Literature',
           'Hobby': 'Swimming'}

# a. Print the whole dictionary
print('Student Initialized: ------------------------------------------------------')
print(student, end='\n\n')

# b. Print the keys
print('Student\'s keys: ----------------------------------------------------------')
print(student.keys(), end='\n\n')

# c. Print the values
print('Student\' values: ---------------------------------------------------------')
print(student.values(), end='\n\n')

# d. Bruce changed Course to 'Foreign Languages'
student.update({'Course': 'Foreign Languages'})
print('Student after CHANGED course: ---------------------------------------------')
print(student)

# e. Add missing 'Address' and 'Phone number', use 2 methods
student['Address'] = '23/22 Vo Van Kiet.tr'
student.update({'Phone number': '0123456789'})
print('Student after added Address and Phone number: -----------------------------')
print(student)

# f. Delete 'Sex' and 'Hobby'
del student['Sex']
student.pop('Hobby')
print('Student after DELETED Sex and Hobby: --------------------------------------')
print(student)
