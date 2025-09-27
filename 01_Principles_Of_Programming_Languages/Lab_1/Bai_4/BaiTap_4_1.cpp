//So sánh tuổi của hai người có ngày tháng năm sinh lần lượt là D1, M1 Y1 (đối với người thứ nhất) và D2, M2, Y2 (đối với người thứ hai)
// Compare the ages of two people with birth dates D1, M1, Y1 (for the first person) and D2, M2, Y2 (for the second person)
#include <iostream>
using namespace std;

int Nguoi1, D1, M1, Y1;
int Nguoi2, D2, M2, Y2;
string Ketqua;

bool DateCheck(int day,int month)
{
    return (day <= 31) && (month <= 12);
}

int main()
{
    cout << "Moi nhap [Ngay Thang Nam] sinh cua nguoi thu nhat: ";
    cin >> D1 >> M1 >> Y1;
    if(!DateCheck(D1,M1))
    {
        cout << "Ngay Thang khong hop le!" << endl;
        return 1;
    }
    cout << "Moi nhap [Ngay Thang Nam] sinh cua nguoi thu nhat: ";
    cin >> D2 >> M2 >> Y2;
    if(!DateCheck(D2,M2))
    {
        cout << "Ngay Thang khong hop le!" << endl;
        return 1;
    }
    
    if(Y1 == Y2)
    {
        if(M1 == M2)
        {
            if(D1 == D2)
            {
                Nguoi1 == Nguoi2;
            }
            else if (D1 > D2)
            {
                Nguoi1 < Nguoi2;
            }
            else
            {
                Nguoi1 > Nguoi2;
            }
        }
        else if (M1 > M2)
        {
            Nguoi1 < Nguoi2;
        }
        else
        {
            Nguoi1 > Nguoi2;
        }
        
    }
    else if (Y1 > Y2)
    {
        Nguoi1 < Nguoi2;
    }
    else
    {
        Nguoi1 > Nguoi2;
    }
    
    if(Nguoi1 > Nguoi2)
    {
        Ketqua = "Nguoi thu nhat lon hon nguoi thu hai!";
    }
    else
    {
        Ketqua = "Nguoi thu hai lon hon nguoi thu nhat!";
    }

    cout << "Ket qua: " << Ketqua << endl;
    return 0;
}