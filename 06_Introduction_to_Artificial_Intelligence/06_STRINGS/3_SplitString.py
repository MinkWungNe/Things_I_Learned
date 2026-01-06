'''
Cho 1 Chuỗi như sau “5;7;8;-2;8;11;13;9;10” (có thể nhập bất kỳ từ bàn phím)
-	xuất các chữ số trên các dòng riêng biệt
-	Xuất có bao nhiêu chữ số chẵn
-	Xuất có bao nhiêu số âm
-	Xuất có bao nhiêu chữ số nguyên tố
-	Tính giá trị trung bình
------------------------------------------------------------------------------
Let a string like this "5;7;8;-2;8;11;13;9;10" (can be entered from the keyboard)
-	Print the numbers on separate lines
-	Print how many even numbers there are
-	Print how many negative numbers there are
-	Print how many prime numbers there are
-	Calculate the average value
'''
def CheckPrime(x):
    dem=0
    for i in range(1,x+1):
        if x % i ==0:
            dem+=1
    return dem==2
s="5;7;8;-2;8;11;-13;9;10"
arr=s.split(';')
sochan=0
soam=0
sont=0
sum=0
for x in arr:
    print(x)
    number=int(x)
    if number %  2 ==0:
        sochan+=1
    if number <0:
        soam+=1
    if CheckPrime(number):
        sont+=1
    sum=sum+number
print("Số chẵn =",sochan)
print("Số âm =",soam)
print("Số Nguyên tố =",sont)
print("Trung bình=",sum/len(arr))
