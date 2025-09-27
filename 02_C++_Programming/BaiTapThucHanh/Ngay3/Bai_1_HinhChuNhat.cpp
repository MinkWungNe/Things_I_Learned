/*
    Write a C++ program to implement the class rectangleType. The class contains:
    - Two private data members length and width of type double.
    - A public member function setDimension that sets the length and width of the rectangle.
    - A public member function getLength that returns the length of the rectangle.
    - A public member function getWidth that returns the width of the rectangle.
    - A public member function area that returns the area of the rectangle.
    - A public member function perimeter that returns the perimeter of the rectangle.
    - A public member function print that prints the length, width, area and perimeter of the rectangle.
    - A default constructor that initializes length and width to 0.0.
    - A parameterized constructor that takes two arguments to initialize length and width.
    Then, write a class boxType that is derived from the class rectangleType. The class contains:
    - A private data member height of type double.
    - A public member function setDimension that sets the length, width and height of the box.
    - A public member function getHeight that returns the height of the box.
    - A public member function area that returns the surface area of the box.
    - A public member function volume that returns the volume of the box.
    - A public member function print that prints the length, width, height, surface area and volume of the box.
    - A default constructor that initializes height to 0.0 and calls the default constructor of the base class.
    - A parameterized constructor that takes three arguments to initialize length, width and height and calls the parameterized constructor of the base class.
    Finally, write a main function to test the classes.
*/

#include <iostream>
using namespace std;

//---------------------------- Rectangle Type ------------------------------------------
class rectangleType
{
    private:
        double length;
        double width;
    
    public:
        void setDimension(double l, double w);
        double getLength() const;
        double getWidth() const;
        double area() const;
        double perimeter() const;
        void print() const;
        rectangleType();
        rectangleType(double l,double w); 
};

void rectangleType::setDimension(double l, double w)
{
    length = l;
    width = w;
}

double rectangleType::getLength() const
{
    return length;
}

double rectangleType::getWidth() const
{
    return width;
}

double rectangleType::area() const
{
    return (length*width);
}

double rectangleType::perimeter() const
{
    return 2*(length + width);
}

void rectangleType:: print() const
{
    cout <<"Chieu dai: " << length << endl;
    cout <<"Chieu ngang: " << width << endl;
    cout <<"Dien tich: " << area() << endl;
    cout << "Chu vi: " << perimeter() << endl << endl;
}

rectangleType::rectangleType()
{
    length = 0.0;
    width = 0.0;
}
rectangleType::rectangleType(double l, double w)
{
    length = l;
    width = w;
}


//---------------------------- Box Type >> Rectangle Type ------------------------------------------
class boxType: public rectangleType
{
    private:
        double height;
    
    public:
        void setDimension(double l, double w, double h);
        double getHeight() const;
        double area() const;                                    //Dien Tich
        double volume() const;                                  //The tich
        void print() const;
        boxType();
        boxType(double l, double w, double h);
};

void boxType::setDimension(double l, double w, double h)
{
    rectangleType::setDimension(l,w);
    if(h >= 0)
    {
        height = h;
    }
    else 
    {
        height = 0.0;
    }
}

double boxType::getHeight() const 
{
    return height;
}

double boxType::area() const
{
    return 2*(getLength()*getWidth() + getLength()*height + getWidth()*height);
}

double boxType::volume() const
{
    return rectangleType::area()* height;           //or return( getLength() * getWidth * height )
}

void boxType::print() const
{
    cout << "Chieu dai: " << getLength() << endl;
    cout << "Chieu rong: " << getWidth() << endl;
    cout << "Chieu cao: " << height << endl;
    cout << "Dien tich: " << area() << endl;
    cout << "The tich: " << volume() << endl << endl;
}

boxType::boxType():rectangleType()
{
    height = 0.0;
}

boxType::boxType(double l, double w, double h):rectangleType(l,w)
{
    height = h;
}




int main()
{
    // rectangleType hinh1;
    // hinh1.print();

    // rectangleType hinh2(5,10);
    // hinh2.print();

    boxType hop1;
    hop1.print();

    boxType hop2(5, 10, 15);
    hop2.print();
}