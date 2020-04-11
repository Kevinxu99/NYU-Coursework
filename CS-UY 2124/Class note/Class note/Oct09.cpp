//
//  Oct09.cpp
//  Class note
//
//  Created by Kevin Xu on 10/9/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
using namespace std;

class Vector {
public:
    Vector() : theSize(0), theCapacity(4), data(new int[theCapacity]) {}
    
    explicit Vector(size_t count, int value = 0) {
        theSize = count;
        theCapacity = count;
        data = new int[count];
        for(size_t i = 0; i < count ; ++i) {
            data[i] = value;
        }
    }
    
    //Copy control
    ~Vector() {
        delete[] data;
    }
    
    Vector(const Vector& rhs) {
        theSize = rhs.theSize;
        theCapacity = rhs.theCapacity;
        data = new int[theCapacity];
        for (size_t i=0; i < theSize; ++i) {
            data[i] = rhs.data[i];
        }
    }
    
    Vector& operator=(const Vector& rhs) {
        //1. Self assignment
        if (this != &rhs) {
            //2. free up
            delete[] data;
            //3. allocate
            data = new int[rhs.theCapacity];
            //4. copy
            theSize = rhs.theSize;
            theCapacity = rhs.theCapacity;
            for (size_t i=0; i < theSize; ++i) {
                data[i] = rhs.data[i];
            }
        }
        //return myself
        return *this;
    }
    
    void push_back(int val) {
        if (theSize == theCapacity) {
            int* old = data;
            data = new int[2*theCapacity];
            for (size_t i = 0; i < theSize; ++i) {
                data[i] = old[i]; //pointer arithmetic
            }
            delete[] old;
            theCapacity *= 2;
        }
        data[theSize] = val;
        ++theSize;
    }
    
    size_t size() const{
        return theSize;
    }
    void clear() {
        theSize = 0;
    }
    void pop_back() {
        --theSize;
    }
    
    //Square brackets?
    int operator[](size_t index) const{
        return data[index];
    }
    int& operator[](size_t index) {//return by reference
        return data[index];
    }
    
    //int* begin() {return &data[0];}
    int* begin() {return data;}
    //int* end() {return &data[theSize];}
    int* end() {return data + theSize;}
private:
    size_t theSize;
    size_t theCapacity;
    int* data;
};

int main() {
    Vector v; //Not templated. Our Vector class can only hold ints
    v.push_back(17);
    v.push_back(42);
    v.push_back(6);
    v.push_back(28);
    
    for (size_t i = 0; i > v.size(); ++i) {
        cout << v[i] << endl;
    }
    
    v[0] = 100;
    
    for (int x : v) {
        cout << x << ' ';
    }
    
    for (int* p = v.begin(); p != v.end(); ++p) {
        int x = *p;
        cout << x << ' ';
        //cout << *p << ' ';
    }
}
