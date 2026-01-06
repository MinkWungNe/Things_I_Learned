'''
Trích lọc số âm trong chuỗi.
Viết một hàm đặt tên là NegativeNumberInStrings(str). Hàm này có đối số truyền vào là một chuỗi bất kỳ, 
Hãy viết lệnh để xuất ra các số nguyên âm trong chuỗi.
Ví dụ: Nếu nhập vào chuỗi “abc-5xyz-12k9l--p” thì hàm phải xuất ra được 2 số nguyên âm đó là -5 và -12
------------------------------------------------------------------------------------------------------------------
Attract negative numbers in a string.
Write a function named NegativeNumberInStrings(str). The function takes a string as its argument.
Write code to extract the negative integers from the string.
For example: If the input string is "abc-5xyz-12k9l--p" then the function should return -5 and -12.
'''

def NegativeNumberInStrings(s):
    import re
    # Sử dụng biểu thức chính quy để tìm các số âm trong chuỗi
    negative_numbers = re.findall(r'-\d+', s)
    return negative_numbers

# Test the function
input_string = "abc-5xyz-12k9l--p"
result = NegativeNumberInStrings(input_string)
print("Negative numbers in the string:", result)