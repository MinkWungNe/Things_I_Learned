// Viết chương trình tìm chữ ‘i’ và thay bằng chử in hoa. Tức là i → I
// Write a program to find the letter 'i' and replace it with the uppercase letter 'I'. That is, i → I
#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    char CauNoi[] = "Hoc, hoc nua, hoc mai. Co chi thi nen";   // It's a sentence in Vietnamese meaning "Study, study more, study forever. If you have a will, you will succeed"
    char *ptc;
    int Length = strlen(CauNoi);
    
    for (int i = 0; i < Length;i++)
    {
        ptc = & CauNoi[i];
        if (CauNoi[i] == 'i' )
        {
            *ptc = 'I';
        }
    }
    
    cout << CauNoi << endl;

}