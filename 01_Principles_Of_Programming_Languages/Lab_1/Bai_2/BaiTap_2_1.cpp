//Tính chu vi P của một hình tròn có bán kính R nhập từ bàn phím    
//Calculate the perimeter P of a circle with radius R input from the keyboard
#include <iostream>
using namespace std;

int main()
{
    float R, P;
    const float PI = 3.14;
    cout << "Nhap ban kinh R: "; cin >> R;
    P = 2*PI*R;
    cout << "Chu vi hinh tron: " << P << endl;
}