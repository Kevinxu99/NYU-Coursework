//
//  Oct15.cpp
//  Class note
//
//  Created by Kevin Xu on 10/15/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

class FrogPrince;

class Princess {
public:
    //Princess(const string& name) : name(name) {}
    Princess(const string& name);
    void display() const; // const is a part of the prototype
    
    void marries(FrogPrince& betrothed);
    
private:
    string name;
    FrogPrince* spouse;
    //FrogPrince spouse; wouldn't compile because it doesn't know how much memory it needs for FrogPrince
};

class FrogPrince {
public:
    FrogPrince(const string& name);
    void display() const;
    void setSpouse(Princess* pp);
private:
    string name;
    Princess* spouse;
};

int main() {
    Princess snowy("Snow White");
    snowy.display();
}

void Princess::marries(FrogPrince& betrothed) {
    spouse = &betrothed;
    betrothed.setSpouse(this);
}

void Princess::display() const {cout << "Princess: " << name << endl;}

Princess::Princess(const string& name) : name(name) {}

FrogPrince::FrogPrince(const string& name) : name(name) {}
void FrogPrince::display() const {cout << "Frog: " << name << endl;}
void FrogPrince::setSpouse(Princess* pp) {spouse = pp;}
