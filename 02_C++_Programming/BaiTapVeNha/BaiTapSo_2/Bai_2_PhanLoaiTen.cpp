// Viết chương trình nhập 10 tên bất kì và sắp xếp theo thứ tự ABC.  Hiển thị danh sách trước khi săp xếp và sau khi sắp xếp.
// Write a program to enter any 10 names and sort them in ABC order. Display the list before and after sorting.
#include <iostream>
#include <cstring>
using namespace std;
#define SoHocSinh 10
#define ChieuDaiTen 50

int main()
{
    int i,j,count = 0;
    char ds[SoHocSinh][ChieuDaiTen];
    char *ptr[SoHocSinh], *tmp;

    while (count < SoHocSinh)
    {
        cout << "Hoc sinh thu " << count + 1 << " : ";
        cin >> ds[count];
        if (strlen( ds[count] ) == 0 ) break;
        ptr[count] = &ds[count][0];
        ++count;
    }
    
    for (i = 0 ; i < count - 1; i++)
    {
        for (j = i + 1 ; j < count ; j++)
        {
            if (strcmp(ptr[i],ptr[j]) > 0 )
            {
                tmp = ptr[i]; ptr[i] = ptr[j] ; ptr[j] = tmp;
            }
        }
    }

    cout << "Danh sach chua phan loai: " << endl;
    for (i = 0; i <count ; i++)
    {
        cout << i + 1 << ". " << ds[i] << endl;
    }
    cout << endl << "Danh sach da phan loai: " << endl;
    for (i = 0; i <count ; i++)
    {
        cout << i + 1 << ". " << ptr[i] << endl;
    }
}