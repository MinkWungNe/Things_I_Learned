//Cho 2 đường tròn. Tính số điểm mà chúng cắt nhau.
//Given 2 circles. Calculate the number of intersection points.
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    double x1, y1, x2, y2;
    double r1, r2;
    string SoDiemCatNhau;
    cout << "Nhap x1 y1 va ban kinh R1: ";
    cin >> x1 >> y1 >> r1;
    cout << "Nhap x2 y2 va ban kinh R2: ";
    cin >> x2 >> y2 >> r2;

    double KhoangCach = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
    double R = r1 + r2;

    if(KhoangCach < R)
    {
        SoDiemCatNhau = "Hai duong tron cach nhau 2 diem.";
    }
    else if(KhoangCach == R)
    {
        SoDiemCatNhau = "Hai duong tron tiep xuc voi nhau 1 diem.";
    }
    else 
    {
        SoDiemCatNhau = "Hai duong tron khong cat nhau";
    }
    cout << "Ket qua: " << SoDiemCatNhau << endl;
    return 0;
}