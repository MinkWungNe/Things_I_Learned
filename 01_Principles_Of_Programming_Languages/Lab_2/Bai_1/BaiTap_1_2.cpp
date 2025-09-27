//Cho 2 số nguyên dương a và b. Kiểm tra xem a có chia hết cho b không? Lưu ý số nguyên dương là số lớn hơn hoặc bằng 0.
//Let a, b be two positive integers. Check if a is divisible by b. Note that a positive integer is a number greater than or equal to 0.
#include <iostream>
using namespace std;

int NguyenDuongCheck(int num)
{
    if(num <0)
    {
        cout << "Vui long nhap so nguyen duong" << endl;
        return 1;
    }
    else
    {
        return 0;
    }
}

int main()
{
    int a, b;
    string Ketqua;
    
    cout << "Nhap a: ";
    cin >> a;
    NguyenDuongCheck(a);
    cout << "Nhap b: ";
    cin >> b;
    NguyenDuongCheck(b);

    if (a % b == 0)
    {
        Ketqua = "Ket qua: a chia het cho b";
    }
    else
    {
        Ketqua = "Ket qua: a khong chia het cho b";
    }
    cout << Ketqua << endl;
    return 0;
}
