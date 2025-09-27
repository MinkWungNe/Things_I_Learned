//Hãy viết 1 chương trình hoán vị 2 số nguyên dương không sử dụng biến trung gian.
//Write a program to swap 2 positive integers without using a temporary variable.
#include <iostream>
using namespace std;

int main()
{
    int a,b;
    cout << "Nhap a: "; cin >> a;
    cout << "Nhap b: "; cin >> b;
    a = a + b;
    b = a - b;
    a = a - b;
    cout << "Sau khi hoan vi: a= " << a << " b= " << b << endl;
    return 0;
}