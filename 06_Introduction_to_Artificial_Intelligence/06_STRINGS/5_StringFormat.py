'''
Xử lý chuỗi với các hàm cơ bản
Viết chương trình cho phép nhập vào 1 chuỗi. Yêu cầu xuất ra:
-	Bao nhiêu chữ IN HOA
-	Bao nhiêu chữ in thường
-	Bao nhiêu chữ là chữ số
-	Bao nhiêu chữ là ký tự đặc biệt
-	Bao nhiêu chữ là khoảng trắng
-	Bao nhiêu chữ là Nguyên Âm
-	Bao nhiêu chữ là Phụ âm
----------------------------------------------------------------
Format string with basic functions
Write a program that allows you to enter a string. The program should output:
- How many uppercase letters
- How many lowercase letters
- How many digits
- How many special characters
- How many whitespace characters
- How many vowels
- How many consonants
'''

def count_string_features(input_string):
    uppercase_count = sum(1 for c in input_string if c.isupper())
    lowercase_count = sum(1 for c in input_string if c.islower())
    digit_count = sum(1 for c in input_string if c.isdigit())
    special_char_count = sum(1 for c in input_string if not c.isalnum() and not c.isspace())
    whitespace_count = sum(1 for c in input_string if c.isspace())
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for c in input_string if c in vowels)
    consonant_count = sum(1 for c in input_string if c.isalpha() and c not in vowels)

    return {
        'uppercase': uppercase_count,
        'lowercase': lowercase_count,
        'digits': digit_count,
        'special_characters': special_char_count,
        'whitespaces': whitespace_count,
        'vowels': vowel_count,
        'consonants': consonant_count
    } 

# Input from user
user_input = input("Enter a string: ")
result = count_string_features(user_input)
print("String analysis results:")
for feature, count in result.items():
    print(f"{feature.capitalize()}: {count}")  
    