'''
Dãy Số Fibonacci là dãy số có dạng:
1-1-2-3-5-8-13-21-34-55-89…
Được định nghĩa theo công thức đệ qui như dưới đây:
Nếu N=1,N=2->FN=1
    N>2 FN=FN-1+FN-2
Hãy viết 2 hàm:
 - Hàm trả về số Fib tại vị trí thứ N bất kỳ
 - Hàm trả về danh sách dãy số Fib từ 1 tới N

Fibonacci number is a series of numbers looking like:
1-1-2-3-5-8-13-21-34-55-89...
It is defined by the following recursive formula:
If  N=1,N=2->FN=1
    N>2 FN=FN-1+FN-2
Write 2 functions:
 - A function that returns the Fibonacci number at any given position N
 - A function that returns the list of Fibonacci numbers from 1 to N
'''
def fibonacci(n):
    if n<=2 :
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def listfibo(n):
    for i in range(1,n+1):
        print(fibonacci(i),end='\t')

print(fibonacci(9))

listfibo(9)
