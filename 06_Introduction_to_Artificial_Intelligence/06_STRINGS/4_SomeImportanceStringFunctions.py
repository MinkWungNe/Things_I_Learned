'''
Trình bày một số hàm quan trọng trong xử lý Chuỗi của Python
'''
# Chuỗi trong Python là bất biến (immutable)
# Một số hàm quan trọng trong xử lý chuỗi:
s = "  Hello, World!  "
print(s.lower())        # Chuyển chuỗi thành chữ thường
print(s.upper())        # Chuyển chuỗi thành chữ hoa
print(s.strip())        # Loại bỏ khoảng trắng ở đầu và cuối chuỗi
print(s.replace("World", "Python"))  # Thay thế "World" bằng "Python"
print(s.split(","))     # Tách chuỗi thành danh sách tại dấu phẩy
print(s.find("World"))  # Tìm vị trí của "World" trong chuỗi
print(s.startswith("  He"))  # Kiểm tra chuỗi bắt đầu bằng "  He"
print(s.endswith("!  "))      # Kiểm tra chuỗi kết thúc bằng "!  "
print(s.count("o"))     # Đếm số lần xuất hiện của "o" trong chuỗi
print(s.isalpha())      # Kiểm tra chuỗi có chỉ chứa chữ cái không
print(s.isdigit())      # Kiểm tra chuỗi có chỉ chứa chữ số không
print(s.isspace())      # Kiểm tra chuỗi có chỉ chứa khoảng trắng không
print(s.title())       # Chuyển đổi chuỗi thành dạng tiêu đề (mỗi từ viết hoa chữ cái đầu)
print(s.capitalize())  # Viết hoa chữ cái đầu tiên của chuỗi
print(s.center(30, '*'))  # Căn giữa chuỗi trong một chuỗi dài 30 ký tự, dùng '*' để lấp đầy
print(s.zfill(30))     # Đệm chuỗi với các số 0 ở bên trái để đạt độ dài 30 ký tự
print(s.encode('utf-8'))  # Mã hóa chuỗi thành bytes sử dụng UTF-8
print(s.format())      # Định dạng chuỗi (thường dùng với f-strings trong Python 3.6+)
print(s.join(['Python', 'is', 'fun']))  # Nối các chuỗi trong danh sách với chuỗi s làm dấu phân cách
print(s.partition(","))  # Chia chuỗi thành ba phần tại dấu phẩy đầu tiên
print(s.rpartition("!")) # Chia chuỗi thành ba phần tại dấu chấm than cuối cùng
print(s.rsplit(" ", 1)) # Tách chuỗi từ phải sang trái, tối đa 1 lần
print(s.swapcase())     # Đổi chữ hoa thành chữ thường và ngược lại trong chuỗi
print(s.translate(str.maketrans("Helo", "hELo")))  # Thay thế các ký tự theo bảng dịch
print(s.removeprefix("  "))  # Loại bỏ tiền tố "  "nếu có (Python 3.9+)
print(s.removesuffix("  "))  # Loại bỏ hậu tố "  "nếu có (Python 3.9+)
print(s.partition("o"))  # Chia chuỗi thành ba phần tại ký tự 'o' đầu tiên
print(s.rpartition("o")) # Chia chuỗi thành ba phần tại ký tự 'o' cuối cùng
print(s.splitlines())   # Tách chuỗi thành danh sách tại các dòng mới  (nếu có)
print(s.isprintable())  # Kiểm tra chuỗi có chỉ chứa ký tự in được không
print(s.isidentifier()) # Kiểm tra chuỗi có phải là một định danh hợp lệ trong Python không
print(s.removeprefix("  "))  # Loại bỏ tiền tố "  "nếu có (Python 3.9+)
print(s.removesuffix("  "))  # Loại bỏ hậu tố "  "nếu có (Python 3.9+)
print(s.partition("o"))  # Chia chuỗi thành ba phần tại ký tự 'o' đầu tiên
print(s.rpartition("o")) # Chia chuỗi thành ba phần tại ký tự 'o' cuối cùng
print(s.splitlines())   # Tách chuỗi thành danh sách tại các dòng mới  (nếu có)
print(s.isprintable())  # Kiểm tra chuỗi có chỉ chứa ký tự in được không
print(s.isidentifier()) # Kiểm tra chuỗi có phải là một định danh hợp lệ trong Python không
print(s.encode('utf-8'))  # Mã hóa chuỗi thành bytes sử dụng UTF-8
print(s.format())      # Định dạng chuỗi (thường dùng với f-strings trong Python 3.6+)
print(s.join(['Python', 'is', 'fun']))  # Nối các chuỗi trong danh sách với chuỗi s làm dấu phân cách
print(s.partition(","))  # Chia chuỗi thành ba phần tại dấu phẩy đầu tiên
print(s.rpartition("!")) # Chia chuỗi thành ba phần tại dấu chấm than cuối cùng
print(s.rsplit(" ", 1)) # Tách chuỗi từ phải sang trái, tối đa 1 lần
print(s.swapcase())     # Đổi chữ hoa thành chữ thường và ngược lại trong chuỗi
print(s.translate(str.maketrans("Helo", "hELo")))  # Thay thế các ký tự theo bảng dịch
print(s.removeprefix("  "))  # Loại bỏ tiền tố "  "nếu có (Python 3.9+)
print(s.removesuffix("  "))  # Loại bỏ hậu tố "  "nếu có (Python 3.9+)
print(s.partition("o"))  # Chia chuỗi thành ba phần tại ký tự 'o' đầu tiên
print(s.rpartition("o")) # Chia chuỗi thành ba phần tại ký tự 'o' cuối cùng
print(s.splitlines())   # Tách chuỗi thành danh sách tại các dòng mới  (nếu có)
print(s.isprintable())  # Kiểm tra chuỗi có chỉ chứa ký tự in được không
print(s.isidentifier()) # Kiểm tra chuỗi có phải là một định danh hợp lệ trong Python không