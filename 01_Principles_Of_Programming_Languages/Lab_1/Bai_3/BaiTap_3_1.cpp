//So sánh diện tích A1 của một hình vuông có cạnh E với diện tích của một hình tròn có bán kính R
//Compare the area A1 of a square with side E and the area of a circle with radius R
#include <iostream>
using namespace std;

int main()
{
    float A1, E;
    float HinhTron, R;
    string Ketqua;
    cout << "Nhap canh hinh vuong E: ";
    cin >> E;
    cout << "Nhap duong kinh hinh tron R: ";
    cin >> R;

    A1 = E*E;
    HinhTron = R*R*3.14;
    if(A1 > HinhTron)
    {
        Ketqua = "Hinh vuong A1 co dien tich lon hon";
    }
    else
    {
        Ketqua = "Hinh tron co dien tich lon hon";
    }

    cout << "Ket qua la: " << endl << Ketqua << endl;
    return 0;
}