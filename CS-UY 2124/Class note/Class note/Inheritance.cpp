//
//  Inheritance.cpp
//  Class note
//
//  Created by Kevin Xu on 10/24/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Pet {
public:
    Pet(const string& name) : name(name) {}
    virtual void eat() {cout << "eating\n";}
    virtual ~Pet() {}
private:
    string name;
protected:
    //string name;//fields should be private;
    const string& getName() const {return name;} //only Cat can access
};

class Cat : public Pet {
public:
    Cat(const string& name) : Pet(name) {} //delegate the Pet constructor to initialize name
    void eat() override{cout << "cat eating\n";} //check if there is a virtual method in the base class
    //with the same signature. show error if can't find one.
    void purr() {cout << "purring\n";};
private:
    //string name;
};
class Slug : public Pet {
public:
    using Pet::Pet;
};
class Roach : public Pet {
public:
    using Pet::Pet;
};

void silly(Pet aPet) {//slicing
    cout << "passed in a pet" << endl;
}

int main() {
    Pet peeve("Peeve");
    silly(peeve);
    
    Cat felix("Felix"); //don't inherite constructor
    felix.eat();
    
    silly(felix);
    
    Slug sluggo("Sluggo");
    
    peeve = felix;
    //felix = peeve;
    //Roach archie;
    
    /*vector<Pet> menagerie;
    menagerie.push_back(felix);
    menagerie.push_back(peeve);
    menagerie.push_back(sluggo);
    menagerie.push_back(archie);
    for (size_t i = 0; i < menagerie.size(); ++i) {
        menagerie[i].eat();
    }*/
    
    vector<Pet*> menagerie;
    menagerie.push_back(&felix);
    menagerie.push_back(&peeve);
    menagerie.push_back(&sluggo);
    //menagerie.push_back(&archie);
    for (size_t i = 0; i < menagerie.size(); ++i) {
        menagerie[i]->eat();
    }
    
    Pet* petPtr = &peeve;
    petPtr->eat();
    petPtr = &felix;
    petPtr->eat();
    //petPtr->purr();
    //compiler doesn't know what the petPtr is pointing to. can only call methods in the Pet class
    
    Cat* catPtr = &felix;
    catPtr->eat();
    catPtr->purr();
    
    //catPtr = petPtr;
    petPtr = catPtr;
}

/* Polymorphism
 to use polymorphism, mark the methods as virtual
 increases the runtime
 */
