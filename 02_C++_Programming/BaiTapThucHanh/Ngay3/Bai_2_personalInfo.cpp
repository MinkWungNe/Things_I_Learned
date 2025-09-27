// Write a program that uses the personalInfo class to create an object and display the personal information.
#include <iostream>
#include "personalInfo.h"
using namespace std;

int main()
{
    personalInfo nhanvien("Nguyen Van", "Teo", 12,5,2005,25);
    nhanvien.printPersonalInfo();
    return 0;
}