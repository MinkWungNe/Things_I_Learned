/* 
Cho dãy số sau: int arr[] = { 1, 4, 2, 3, 6, 5, 8, 9, 7 }; viết chương trình 
    1) sắp xếp dãy số trên từ bé tới lớn. 
    2) Cho phép người dùng nhập 1 số tìm kiếm bất kì. Nếu có số đó trong dãy trên thì trả về vị trí của số đó. Ngược lại hiện thị kết quả “Không tìm thấy”. Sử dụng phương pháp nhị phân.
*/
/*
Let the following array: int arr[] = { 1, 4, 2, 3, 6, 5, 8, 9, 7 }; write a program
    1) sort the above array from smallest to largest.
    2) Allow users to enter any search number. If that number is in the above array, return its position. Otherwise, display the result "Not found". Use the binary method.
*/
#include <iostream>
using namespace std;

void BubbleSort(int arr[])
{
    for (int i = 0; i < 9 - 1; i++)             // Kiểm tra nếu i bé hơn chiều dài của dãy số
        {
            for (int j = i + 1; j < 9; j++)
            {
                if (arr[i] > arr[j])                 // Nếu GIÁ TRỊ của số đầu > số sau
                {
                    int tmp = arr[i];              // Biến tạm để chứa i 
                    arr[i] = arr[j];                 // i rỗng chứa j
                    arr[j] = tmp;                  // j rỗng chứa biến tạm (i)
                }
            }
        }
}

int BinarySearch(int arr[], int Trai, int Phai, int SoCanTim)
{
    while (Trai <= Phai) 
    {
        int mid = Trai + (Phai - Trai) / 2;
        if (arr[mid] == SoCanTim) 
        {
            return mid;
        }
        if (arr[mid] < SoCanTim) 
        {
            Trai = mid + 1; // Tìm kiếm nửa bên phải
        } 
        else 
        {
            Phai = mid - 1; // Tìm kiếm nửa bên trái
        }
    }
    return -1;
}

int main()
{
    int arr[9] = {1, 4, 2, 3, 6, 5, 8, 9, 7};
    int Size = sizeof(arr) / sizeof(arr[0]);
    int Input;

    // Sắp xếp mảng
    BubbleSort(arr);
    cout << "Mang da duoc sap xep: ";
    for (int i = 0; i < 9; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl; 

    // Tìm kiếm Bằng Phương Pháp Nhị Phân
    cout << "Moi chon so de tim kiem: ";
    cin >> Input;
    int KetQua = BinarySearch(arr, 0, Size - 1, Input);
    if (KetQua != -1)
    {
        cout << "Da tim thay so [" << Input << "] tai vi tri: " << KetQua << endl;
    }
    else 
    {
        cout << "Khong tim thay ket qua can tim..." << endl;
    }
    return 0;
}