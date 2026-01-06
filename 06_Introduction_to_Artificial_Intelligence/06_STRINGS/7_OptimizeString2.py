'''
Tối ưu chuỗi danh từ
Viết chương trình tối ưu Chuỗi danh từ
Một Chuỗi được gọi là tối ưu khi: Không chứa các khoảng trắng dư thừa, các từ cách nhau bởi một khoảng trắng, Ký tự đầu tiên của các từ Viết Hoa
Ví dụ:
Input “     TRần    duY            thAnH   ”
Output “Trần Duy Thanh”

------------------------------------------------
Optimized Noun String
Write a program to optimize Noun String
A String is called optimized when: It does not contain redundant spaces, words are separated by a single space, The first character of the words is Capitalized 
For example:
Input “     TRần    duY            thAnH   ”
Output “Trần Duy Thanh”
'''

def optimize_string(s):
    # Loại bỏ khoảng trắng thừa ở đầu và cuối chuỗi, sau đó tách chuỗi thành các từ
    words = s.strip().split()
    
    # Chuyển đổi mỗi từ: Viết hoa chữ cái đầu và viết thường các chữ cái còn lại
    optimized_words = [word.capitalize() for word in words]
    
    # Nối các từ lại với nhau bằng một khoảng trắng
    optimized_string = ' '.join(optimized_words)
    
    return optimized_string

# Nhập chuỗi từ người dùng
input_string = input("Nhập chuỗi: ")
# Tối ưu chuỗi và in kết quả
output_string = optimize_string(input_string)
print("Chuỗi tối ưu:", output_string)
