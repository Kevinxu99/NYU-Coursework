 //
//  Sept26.cpp
//  Class note
//
//  Created by Kevin Xu on 9/26/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

class Person {
public:
    Person(const string& name) : name(name) {}
    void display(ostream& os = cout) const {
        os << "Name: " << name << "; ";
        if (spouse == nullptr) cout << "Single";
        else cout << "Married to" << spouse->name;
        // << (*spouse).name;  '.' has a higher preference than '*'
            
    }
    
    //void marries(Person betrothed) {
    bool marries (Person& betrothed) {
        if (spouse == nullptr && betrothed.spouse == nullptr) {
            spouse = &betrothed;
            betrothed.spouse = this;
            return true;
        }
        return false;
    }

private:
    string name;
    Person* spouse = nullptr;
};

int main() {
    Person john("John");
    Person mary("Mary");
    john.display();
    mary.display();
    john.marries(mary);
    
    Person sally("Sally");
    sally.marries(john);
    
    int x = 17;
    cout << &x << endl; //address-of operator
    int* p = &x;
    // int *p = &x;
    // int * p = &x;
    
    cout << *p <<endl;
    *p = 42;
    cout << *p <<endl;
    
    /*int* q = &x;
    int* const q1 = &x; //can't change where it points to
    const int* q2 = &x; //can't change what it points to
    
    const int y = 6;*/
    //q = &y;
    //*q = 28;
    
    ifstream ifs("people.txt");
    vector<Person*> people;
    
    string name;
    while (ifs >> name) {
        //Person someone(name);  same memory location with every initialization
        Person* personPtr = new Person(name); //create new Person object in the heap
        //people.push_back(&someone);
        people.push_back(personPtr);
    }
    
    for (Person* pp : people) {
        //cout << pp <<endl;
        pp->display();
    }
    
    //C++ asks us to manage our own memory
    for (Person* pp : people) {
        delete pp; //free up memory(heap space)
    }
    
    Person* pp2 = new Person("fred");
    pp2 = new Person("george"); //memory leak, no way of accessing the address of the previous memory location
    //dangerous in a big loop if don't free up the memory
    
    delete pp2;
    
}
