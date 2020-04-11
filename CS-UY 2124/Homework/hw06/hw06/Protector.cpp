//
//  Protector.cpp
//  hw06
//
//  Created by Kevin Xu on 11/11/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include "Protector.hpp"
#include "Noble.hpp"
#include <iostream>
using namespace std;

namespace WarriorCraft {
    Protector::Protector(const string& name, int str) : name(name), strength(str) {}
    const string& Protector::getLordName() const{
        return lord->getName();
    }
    bool Protector::ifHired() const{
        if(lord == nullptr) return false;
        return true;
    }
    void Protector::getHired(Lord& aLord) {
        lord = &aLord;
    }
    int Protector::getStrength() const{
        return strength;
    }
    const string& Protector::getName() const{
        return name;
    }
    void Protector::change(double ratio) {
        strength = int(strength*(1-ratio));
    }
    bool Protector::quit() { //quit method
        if(lord == nullptr) return false;
        lord->delPro(this);
        lord = nullptr;
        return true;
    }
    
    void Warrior::defend() const{
        cout << getName() << " says: Take that in the name of my lord, " << getLordName();
    }
    
    void Wizard::defend() const{
        cout << "POOF!" << endl;
    }
    void Archer::defend() const{
        cout << "TWANG! ";
        Warrior::defend();
        cout << endl;
    }
    
    void Swordsman::defend() const{
        cout << "CLANG! ";
        Warrior::defend();
        cout << endl;
    }
}
