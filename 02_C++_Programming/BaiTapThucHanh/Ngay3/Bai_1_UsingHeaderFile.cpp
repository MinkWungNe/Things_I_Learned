/*
    Write a program that uses the classes rectangleType and boxType.
    Create an object of type rectangleType and an object of type boxType.
    Call the print function for each object.
    The output should be similar to the following:
    Chieu dai: 1
    Chieu ngang: 1
    Dien tich: 1
    Chu vi: 4
    Chieu dai: 5
    Chieu rong: 10
    Chieu cao: 15
    Dien tich: 250
    The tich: 750
    Note that the default constructor is used to create the object of type rectangleType.
    The parameterized constructor is used to create the object of type boxType.
    (Hint: The default values for length and width are 1.)
*/

#include <iostream>
#include "RectangleLibrary.h"
#include "BoxLibrary.h"
using namespace std;

int main()
{
    rectangleType HinhChuNhat;
    HinhChuNhat.print();

    boxType HinhHop(5, 10, 15);
    HinhHop.print();
}