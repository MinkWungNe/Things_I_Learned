/* 
    Write a C++ program to read a text file named "Thutinh.txt", encrypt its content by shifting 
each character by one ASCII value, and write the encrypted content to a new file named "ThuKhongTinh.txt". 
The program should also display the contents of both files before and after encryption.
*/

// Khai bao
#include <iostream>
#include <fstream>
#include <string>
using namespace std;


// Hien thi
void Hienthi(const string & tenfile)
{
    ifstream InData;
    InData.open(tenfile);
    if (InData.is_open())
    {
        cout << "Found thutinh.txt" << endl;
        string linechar;
        while (getline(InData,linechar))
        {
            cout << linechar << endl;
        }
        InData.close();
    }
    else 
    {
        cout << "Thutinh.txt not found" << endl;
    }


}


// Ma hoa
void Mahoa()
{
    ifstream InPut("Thutinh.txt");
    ofstream OutPut("ThuKhongTinh.txt");

    if (InPut.is_open() && OutPut.is_open())
    {
        char ch;
        while (InPut.get(ch))
        {
            ch++;
            OutPut.put(ch);
        }
        InPut.close();
        OutPut.close();
        cout << "File have been Encrypted!!!" << endl;
    }
    else
    {
        cout << "File not found..." << endl;
    }
    


}



// Ham main()
int main()
{
    string fileName = "Thutinh.txt";
    Hienthi(fileName);
    Mahoa();
    Hienthi("ThuKhongTinh.txt");
    return 0;
}
