//
//  Inheritance3.cpp
//  Class note
//
//  Created by Kevin Xu on 11/5/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include <iostream>
using namespace std;

class Base {
public:
    void foo(int n) const { cout << "Base::foo(n)\n";}
    //Base(const Base& rhs) {}
    virtual ~Base() {
        cerr << "~Base()\n";
    }
};

class Derived : public Base {
public:
    void foo() const {cout << "Derived::foo()\n";}
    //void foo(int n) const {Base::foo(n);}
    using Base::foo;
    Derived() {}
    ~Derived() {}
    Derived(const Derived& rhs) : Base(rhs) {}
    Derived& operator=(const Derived& rhs) {
        this->Base::operator=(rhs);
        cerr << "" ;
        return *this;
    }
    
};

int main() {
    Derived der;
    //der.foo(17) won't compile
    //der.Base::foo(17);
    der.foo(17);
}
