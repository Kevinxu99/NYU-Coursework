//
//  MultipleInheritance.cpp
//  Class note
//
//  Created by Kevin Xu on 11/12/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include <iostream>
using namespace std;

class Person {
public:
    Person(const string& name) : name(name) {}
    /*const string& getName() const{
        return name;
    }*/
private:
    string name;
};

class Student : public Person {
public:
    //Student() {}
    Student(const string& name) : Person(name) {}
    virtual void display() const {cout << "Student\n";}
private:
    //string name;
};

class Instructor : public virtual Person { //virtual inheritance
public:
    Instructor(const string& name) : Person(name) {}
    virtual void display() const {cout << "Instructor\n";}
private:
    string name;
};

class TA : public Student, public Instructor {
public:
    TA(const string& name) : Person(name), Student(name), Instructor(name) {}
    void display() const {
        //cout << Person::getName();
    }
    //using Student::display;
};

int main() {
    TA rohit("Rohit");
    rohit.display();
    //rohit.Student::display();
}
