//
//  Oct22.cpp
//  Class note
//
//  Created by Kevin Xu on 10/22/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include <iostream>
using namespace std;

class Complex{
    friend ostream& operator<<(ostream& os, const Complex& rhs) {
        os << rhs.real << " " << rhs.imaginary;
        return os;
    }
public:
    Complex() : real(0), imaginary(0) {}
    Complex(double real) : real(real), imaginary(0) {}
    Complex(double real, double imag) : real(real), imaginary(imag) {}
    
    //c1 += c2;
    //c1.operator+=(c2)
    Complex& operator+=(const Complex& rhs) {
        real += rhs.real;
        imaginary += rhs.imaginary;
        return *this;
    }
    
    //++c1
    //c1.operator++();
    Complex& operator++() {
        ++real;
        return *this;
    }
    
    //c1++
    Complex operator++(int dummy) {
        Complex original(*this);
        ++real;
        return original;
    }
    
    explicit operator bool() const{ //dosen't have to be operator "bool", whatever type expected
        return real || imaginary;
    }
    
    bool operator==(const Complex& rhs) const {
        return real == rhs.real && imaginary == rhs.imaginary;
    }
    
private:
    double real, imaginary;
};

//c1 = c2 + c3
//operator+(c2, c3);
Complex operator+(const Complex lhs, const Complex rhs) {
    Complex result = rhs;
    result += lhs;
    return result;
}

//binary operators are overloaded as non-member function


int main() {
    Complex c1;
    Complex c2(17);
    Complex c3(3,-5); //3-5i
    cout << "c1: " << c1 << endl
         << "c2: " << c2 << endl
         << "c3: " << c3 << endl;
    
    c1 = c2 + c3;
    operator+(c2, c3);
    //c2.operator+(c3);
    
    c1 += c2;
    //operator+=(c1,c2)
    c1.operator+=(c2);
    
    ++c1;
    c1.operator++();
    
    c1++;
    c1.operator++(0);
    
    if(c1) {cout << "c1 is not 0+0i\n";}
    
    if (c1 == c2) {}
    c1.operator==(c2);
    
    Complex c4(1);
    if (c4 == 1) {}
    c4.operator==(1); //coerce 1 into a complex number
    
    /*if (1 == c4) {}
    1.operator==(c4);*/
    
}
