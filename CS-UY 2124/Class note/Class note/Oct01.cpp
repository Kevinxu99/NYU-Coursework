//
//  Oct01.cpp
//  Class note
//
//  Created by Kevin Xu on 10/1/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
using namespace std;

class Foo {
public:
    Foo(int x) {p = new int(x);}
    void display() const {cout << *p << endl;}
    void setValue(int val) {*p = val;}
    /*void cleanUp() {
        delete p;
        p = nullptr;
    }*/
    ~Foo() {  //Destructor;No return type
        delete p;
        //p = nullptr;
    }
    Foo(Foo& rhs) { //copy constructor //if don't pass by reference, the copy constructor would be called infinitely.
        //p = rhs.p //shallow copy
        //p = new int(*(rhs.p));
        p = new int(*rhs.p); //'.' has a higher precedence than '*'
    }
private:
    int* p;
};

void doNothing(Foo someFoo) {}//create a copy and would run the destructor at the end(when someFoo is out of scope)
//someFoo is a shallow copy of aFoo, which means someFoo is pointing to the same address on the heap
void simpleFunc() {
    Foo aFoo(17);
    aFoo.display();
    //aFoo.cleanUp();
    doNothing(aFoo);
    aFoo.display();
    new int(28);
    aFoo.display();
} // aFoo's destructor would delete the space that is already deleted

int main() {
    simpleFunc();
}

