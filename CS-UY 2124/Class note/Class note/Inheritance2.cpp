//
//  Inheritance2.cpp
//  Class note
//
//  Created by Kevin Xu on 10/31/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include <iostream>
using namespace std;

class Shape { //abstract class(if it has a abstract method)
public:
    Shape(int x, int y) : x(x), y(y) {}
    void move(int x, int y) {this->x = x; this->y = y;}
    //virtual void draw() {cout << "draw stuff\n";}
    virtual void draw() = 0; //pure virtual
    //void comonDrawingCode() { cout << "common drawing code\n";}
private:
    int x,y;
};

//define the method outside the class if want the body
void Shape::draw() { cout << "common drawing code\n";}

class Triangle : public Shape {
public:
    Triangle(int x, int y) : Shape(x, y) {}
    void draw() {cout << "draw triangle\n";}
};

class Circle : public Shape { //if don't define own draw method, it is also abstract
public:
    Circle(int x, int y) : Shape(x, y) {}
    void draw() {Shape::draw();}
protected:
};

int main() {
    //Shape aShape(3, 4); can't create an instance if it's abstract
    Triangle tri(3,4);
    tri.draw();
    //Circle circ(10,10);
}
