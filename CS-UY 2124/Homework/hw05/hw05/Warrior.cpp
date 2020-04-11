//
//  Warrior.cpp
//  hw05
//
//  Created by Kevin Xu on 10/26/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include "Warrior.hpp"
#include "Noble.hpp"
#include <iostream>
#include <string>
using namespace std;

namespace WarriorCraft{
    Warrior::Warrior(const string& name, const int strength) : name(name), strength(strength) {}

    const string& Warrior::getName() const{return name;}

    int Warrior::getStrength() const{return strength;}

    void Warrior::changeStrength(double ratio) {
        strength = int(strength*(1-ratio));
    }

    bool Warrior::ifHired() const{return theNoble != nullptr;}

    void Warrior::getHired(Noble& hirer) {theNoble = &hirer;}

    void Warrior::getFired() {theNoble = nullptr;}

    void Warrior::runaway() {
        cout << name << " flees in terror, abandoning his lord, " << theNoble->getName() << endl;
        theNoble->deleteWarrior(*this);
        theNoble = nullptr;
    }

    ostream& operator<<(ostream& os, const Warrior& warrior) {
        os << warrior.name << ": " << warrior.strength;
        return os;
    }
}

