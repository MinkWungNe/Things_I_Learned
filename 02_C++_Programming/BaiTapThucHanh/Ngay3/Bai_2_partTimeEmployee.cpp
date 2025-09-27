/*
    Write a program that creates a class named partTimeEmployee that is derived from the class personType.
    The class partTimeEmployee should have the following member variables:
        payRate (double): the hourly pay rate
        hoursWorked (double): the number of hours worked
    The class partTimeEmployee should have the following member functions:
        print: a function that prints the first name, last name, pay rate, hours worked, and the total pay (pay rate * hours worked)
        calculatePay: a function that returns the total pay (pay rate * hours worked)
        setNameRateHours: a function that sets the first name, last name, pay rate, and hours worked
        A constructor that receives the first name, last name, pay rate, and hours worked as parameters and uses these parameters to initialize the member variables
    Write a program that creates an object of the class partTimeEmployee, sets the values of the member variables, and then prints the object’s data.
*/
#include <iostream>
#include "partTimeEmployee.h"
using namespace std;

int main()
{
    partTimeEmployee nhanvien("Nguyen Van", "Teo", 1.2, 24);
    nhanvien.print();
    return 0;
}