'''
1. Những câu nói nổi tiếng. Cho chuỗi ký tự sau:
quote = "The future belongs to those who believe in the beauty of their dreams - Eleanor Roosevelt"
Sử dụng các phương thức xâu ký tự để:
    a. Xóa đến những who.
    b. Thay thế belongs về until.
    c. Thêm seems impossible sau future.
    d. Xóa The future.
    e. Thay thế believe in the beauty of their dreams bằng it's done.
    f. Thay thế Eleanor Roosevelt bằng Nelson Mandela.
    g. Thêm It always vào đầu chuỗi ký tự.
Bạn sẽ nhận được câu trích dẫn nào ở cuối? Hãy đảm bảo các từ được phân cách bằng
dấu cách.

'''

quote = "The future belongs to those who believe in the beauty of their dreams - Eleanor Roosevelt"
string = ""

# a. Delete string till 'who'
targetStringIndex = quote.find('those')
string = quote[targetStringIndex :]
print(string)

# b. replace 'belongs to' -> 'until
string = quote.replace('belongs to', 'until')
print(string)