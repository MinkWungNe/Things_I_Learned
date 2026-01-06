'''
2. Độ dài chuỗi. Viết một hàm nhận một danh sách các chuỗi và một số nguyên, và chỉ in
ra các chuỗi có độ dài khớp với số nguyên cho trước. Gọi hàm bằng hai độ dài từ khác nhau.
'''

def print_StringMatchLength(strList: list, strLen: int):
    for string in strList:
        if len(string) == strLen:
            print(string, '- length:', strLen)

lst = ['Not Even Close', 'Short', 'How', 'Help me'] # 14, 5, 3, 7

print_StringMatchLength(lst, 5) # should print 'Short'
print_StringMatchLength(lst, 7) # should print 'Help me'
