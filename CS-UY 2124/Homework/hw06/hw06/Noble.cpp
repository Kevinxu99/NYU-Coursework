//
//  Noble.cpp
//  hw06
//
//  Created by Kevin Xu on 11/11/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include "Noble.hpp"
#include "Protector.hpp"
#include <iostream>
using namespace std;

namespace WarriorCraft {
    Noble::Noble(const string& name) : name(name) {}
    const string& Noble::getName() const{
        return name;
    }
    void Noble::battle(Noble& enemy) {
        cout << name << " battles " << enemy.name << endl;
        if(dead) {
            if(enemy.dead) {
                cout << "Oh, NO! They're both dead! Yuck!" << endl;
                return;
            }
            else {
                cout << "He's dead, " << enemy.name << endl;
                return;
            }
        }
        if(enemy.dead) {
            cout << "He's dead, " << name << endl;
            return;
        }
        defense(); //protectors defend
        enemy.defense();
        int strength = totalStrength();
        int enemy_strength = enemy.totalStrength();
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
    bool Noble::ifDead() const{
        return dead;
    }
    
    bool Lord::hires(Protector& pro) {
        if(pro.ifHired()) return false;
        if(ifDead()) return false;
        pro.getHired(*this);
        protectors.push_back(&pro);
        return true;
    }
    void Lord::delPro(const Protector* aPro) {
        for(size_t i = 0; i<protectors.size(); i++) {
            if(protectors[i] == aPro) {
                protectors[i] = nullptr;
            }
            if(protectors[i-1] == nullptr) {
                protectors[i-1] = protectors[i];
            }
        }
        protectors.pop_back();
    }
    int Lord::totalStrength() const{
        int str = 0;
        for(Protector* pro : protectors) {
            str += pro->getStrength();
        }
        return str;
    }
    void Lord::strengthChange(double ratio) {
        for(Protector* pro : protectors) {
            pro->change(ratio);
        }
    }
    void Lord::defense() const{
        for(Protector* pro : protectors) {
            if(pro->getStrength() != 0) { //if it's not dead
                pro->defend();
            }
        }
    }
    
    PersonWithStrengthToFight::PersonWithStrengthToFight(const string& name, int str) : Noble(name), strength(str) {}
    int PersonWithStrengthToFight::totalStrength() const{
        return strength;
    }
    void PersonWithStrengthToFight::strengthChange(double ratio) {
        strength = int(strength*(1-ratio));
    }
    void PersonWithStrengthToFight::defense() const{return;} //no protectors to defend

}
