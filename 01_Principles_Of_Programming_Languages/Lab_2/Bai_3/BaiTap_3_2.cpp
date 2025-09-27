//Nhập vào phương trình bậc hai. Kiểm tra phương trình có mấy nghiệm (không tính nghiệm phức).
//Insert a quadratic equation. Check how many solutions the equation has (not counting complex solutions).
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    float a, b, c;
    float delta, x1, x2;
    cout << "Phuong trinh ax^2 + bx + c = 0";
    cout << "Nhap gia tri cho a: ";
        cin >> a;

    cout << "Nhap gia tri cho b: ";
        cin >> b;

    cout << "Nhap gia tri cho c: ";
        cin >> c;

    if (a == 0) {
        cout << "Day khong phai la phuong trinh bac hai." << endl;
    }
    else {
        delta = b * b - 4 * a * c;

        if (delta > 0) {
            x1 = (-b + sqrt(delta)) / (2 * a);
            x2 = (-b - sqrt(delta)) / (2 * a);

            cout << "Phuong trinh co hai nghiem: x1 = " << x1 << ", x2 = " << x2 << endl;
        }
        else if (delta == 0) {
            x1 = -b / (2 * a);

            cout << "Phuong trinh co nghiem kep: x1 = x2 = " << x1 << endl;
        }
        else {
            cout << "Phuong trinh vo nghiem." << endl;
        }
    }

    return 0;
}