'''
3. Nhiều số. Viết một hàm nhận một danh sách các số và một số nguyên, và chỉ in ra các
số chia hết cho số nguyên đó. Nếu người dùng không cung cấp số, thì hàm sẽ chia cho 2
theo mặc định. Gọi hàm bằng hai ước số khác nhau. Cuối cùng, gọi hàm mà không có ước số.
'''

def print_Num(numList: list, numInt: int = 2):
    valid = []
    for num in numList:
        if num % numInt == 0:
            valid.append(str(num))
    
    print('Numbers that divided by', numInt, 'is', ' '.join(valid))
    
numList = [1,2,3,4,5,6,7,8,9,10]
print_Num(numList, 3)
print_Num(numList, 4)
print_Num(numList)
