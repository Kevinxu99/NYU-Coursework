//
//  Noble.cpp
//  hw05
//
//  Created by Kevin Xu on 10/26/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include "Noble.hpp"
#include "Warrior.hpp"
#include <iostream>
#include <string>
#include <vector>
using namespace std;

namespace WarriorCraft{
    Noble::Noble(const string& name) : name(name) {}

    const string& Noble::getName() const{return name;}

    bool Noble::hire(Warrior& aWarrior) {
        if(aWarrior.ifHired()) return false;
        if(dead) return false;
        aWarrior.getHired(*this);
        army.push_back(&aWarrior);
        return true;
    }

    bool Noble::deleteWarrior(Warrior& aWarrior) { //delete Warrior from the amry vector
        bool foundWarrior = false;
        for(size_t i = 0; i < army.size(); i++) {
            if(foundWarrior) army[i-1] = army[i];
            if(army[i] == &aWarrior) foundWarrior = true;
        }
        if(!foundWarrior) return false;
        army.pop_back();
        return true;
    }

    bool Noble::fire(Warrior& aWarrior) {
        if(dead) return false;
        if(!deleteWarrior(aWarrior)) return false;
        cout << aWarrior.getName() << ", you're fired! -- " << name << endl;
        aWarrior.getFired();
        return true;
    }

    void Noble::battle(Noble& enemy) {
        cout << name << " battles " << enemy.name << endl;
        if(dead) {
            if(enemy.dead) {
                cout << "Oh, NO! They're both dead! Yuck!" << endl;
                return;
            }
            else {
                cout << "He's dead " << enemy.name << endl;
                return;
            }
        }
        if(enemy.dead) {
            cout << "He's dead " << name << endl;
            return;
        }
        int strength = armyStrength();
        int enemy_strength = enemy.armyStrength();
        if(strength == enemy_strength) {
            cout << "Mutual Annihalation: " << name << " and "
            << enemy.name << " die at each other's hands" << endl;
            dead = true;
            enemy.dead = true;
            //set the strength of Warriors in both Nobles to zero
            strengthChange(1);
            enemy.strengthChange(1);
            return;
        }
        if(strength > enemy_strength) {
            cout << name << " defeats " << enemy.name << endl;
            strengthChange(double(enemy_strength)/double(strength));
            enemy.dead = true;
            enemy.strengthChange(1);//set strength to zero
            return;
        }
        if(strength < enemy_strength) {
            cout << enemy.name << " defeats " << name << endl;
            enemy.strengthChange(double(strength)/double(enemy_strength));
            dead = true;
            strengthChange(1);//set strength to zero
            return;
        }
    }

    int Noble::armyStrength() const{
        int combinedStrength = 0;
        for(const Warrior* i : army) {
            combinedStrength += i->getStrength();
        }
        return combinedStrength;
    }

    void Noble::strengthChange(double ratio) const{
        for(Warrior* i : army) {
            i->changeStrength(ratio);
        }
    }

    ostream& operator<<(ostream& os, const Noble& rhs) {
        cout << rhs.name << " has an army of " << rhs.army.size() << endl;
        for(const Warrior* i : rhs.army) {
            cout << '\t' << *i << endl;
        }
        return os;
    }
}
