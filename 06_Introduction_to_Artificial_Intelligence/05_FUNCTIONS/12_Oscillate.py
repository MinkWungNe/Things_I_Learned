'''
    Cho mã lệnh sau:

    for n in oscillate(-3,5):
        print(n, end='  ')
    print()

    Hãy viết hàm oscillate để khi chạy phần mềm, nó ra kết quả:
-3   3   -2   2   -1   1   0   0   1   -1   2   -2   3   -3   4   -4
-----------------------------------------------------------------------------------------------------
    Let the following code:
    for n in oscillate(-3,5):
        print(n, end='  ')
    print()

    Write a function oscillate so that when running the software, it produces the result:
-3   3   -2   2   -1   1   0   0   1   -1   2   -2   3   -3   4   -4
'''
def oscillate(start, end):
    if start > end:
        return
    for i in range(start, 0):
        yield i
        yield -i
    yield 0
    yield 0
    for i in range(1, end):
        yield i
        yield -i

for n in oscillate(-3,5):
    print(n, end='  ')
print()