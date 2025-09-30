#include <iostream>
#include <cmath>
#include <string>
using namespace std;
const int soluong = 5;

//part 1 ---------------------------------------------------------------------------------------
string danhsachMSSV[soluong] = {"","2305CT2353","2302CT3456","2305CT3999","2304CT0002"};

//part 2----------------------------------------------------------------------------------------
void NhapMSSV()
{
    cout << "Nhap ma so sinh vien: ";
    getline(cin,danhsachMSSV[0]);
}

//part 3 ----------------------------------------------------------------------------------------
void Indanhsach()
{
        cout << "Danh sach sinh vien: " << endl;
    for ( int i = 0; i < soluong; i++)
    {
        cout << i+1 << ". " << danhsachMSSV[i] << endl;
    }
}

//part 4 -----------------------------------------------------------------------------------------
void SapxepDS(string mang[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (mang[j] > mang[j + 1]) {
                // Swap the elements
                swap(mang[j], mang[j + 1]);
            }
        }
    }
}
void IndanhsachMoi()
{
    cout << "Danh sach sau sap xep: " << endl;
    for ( int i = 0; i < 5; i++)
    { 
        cout << i+1 << ". " << danhsachMSSV[i] << endl;
    }
}

//part 5 ------------------------------------------------------------------------------------------
void Timdiachi()
{
    string maxMSSV = "2305CT3999";
    string* ptrDanhsachMSSV = danhsachMSSV;
    for (int i = 1; i < soluong; ++i) {
        if (danhsachMSSV[i] == maxMSSV) {
            cout << "Dia chi cua phan tu chua MSSV lon nhat la: " << (ptrDanhsachMSSV + i) << endl;
            cout << "Gia tri cua phan tu do la: " << danhsachMSSV[i] << endl;
            break;
        }
    }
}
    
int main()
{
    NhapMSSV();
    Indanhsach();
    cout << endl;
    SapxepDS(danhsachMSSV, soluong);
    IndanhsachMoi();
    cout << endl;
    Timdiachi();
}