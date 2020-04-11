//
//  Sept19.cpp
//  Class note
//
//  Created by Kevin Xu on 9/19/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
using namespace std;

class Date {
public:
    Date(int m, int d, int y) : month(m), day(d), year(y) {}
private:
    int month, day, year;
};

class Person {
    friend ostream& operator<<(ostream& os, const Person& rhs);
  /*friend ostream& operator<<(ostream& os, const Person& rhs) {
              os << "Person: name = " << rhs.name;
              return os;
           } (alternative)*/
public:
    Person(const string& name, int m, int d, int y) : name(name), dob(m, d, y) {}
    //has to initialize all the fields that are not primitive. Call the default constructor otherwise.
    void display() const {
        cout<< "Person: name = " << name << endl;
    }
private:
    string name;
    Date dob;
};

ostream& operator<<(ostream& os, const Person& rhs) {
    os << "Person: name = " << rhs.name;
    return os;
}

int main() {
    Person john("John", 9, 19, 2018);
    // john.display();
    // cout << john << endls;
    cout << john;
    //operator<<(cout, john);
    
}
