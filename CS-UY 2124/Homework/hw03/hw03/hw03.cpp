//
//  hw03.cpp
//  hw03
//
//  Created by Kevin Xu on 10/5/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include <stdio.h>
#include <vector>
#include <iostream>
using namespace std;

class Warrior {
    friend ostream& operator<<(ostream& os, const Warrior& warrior) {
        os << "Warrior: " << warrior.name;
        return os;
    };
    
public:
    Warrior(const string& name, const int strength) : name(name), strength(strength) {}
    
    const string& getName() const{
        return name;
    }
    
    int getStrength() const{
        return strength;
    }
    
    void changeStrength(double ratio) {
        strength = int(strength*(1-ratio));
    }
    
    bool ifHired() const{
        return hired;
    }
    
    void getHired() {
        hired = true;
    }
    
    void getFired() {
        hired = false;
    }
    
private:
    string name;
    int strength;
    bool hired = false;
};

class Noble {
public:
    Noble(const string& name) : name(name) {}
    
    bool hire(Warrior& someWarrior) {
        if(someWarrior.ifHired()) return false;
        if(dead) return false;
        someWarrior.getHired();
        army.push_back(&someWarrior);
        return true;
    }
    
    bool fire(Warrior& someWarrior) {
        if(dead) return false;
        bool foundWarrior = false;
        for(size_t i = 0; i < army.size(); i++) {
            if(foundWarrior) army[i-1] = army[i];
            if(army[i]->getName() == someWarrior.getName()) foundWarrior = true;
        }
        army.pop_back();
        cout << someWarrior.getName() << ", you're fired! -- " << name << endl;
        someWarrior.getFired();
        return true;
    }
    
    int armyStrength() {
        int combinedStrength = 0;
        for(const Warrior* i : army) {
            combinedStrength += i->getStrength();
        }
        return combinedStrength;
    }
    
    void strengthChange(double ratio) {
        for(Warrior* i : army) {
            i->changeStrength(ratio);
        }
    }
    
    void battle(Noble& enemy) {
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
            cout << "Mutual Annihalation: " << name << " and " << enemy.name << " die at each other's hands";
            cout << endl;
            dead = true;
            enemy.dead = true;
            return;
        }
        if(strength > enemy_strength) {
            cout << name << " defeats " << enemy.name << endl;
            strengthChange(enemy_strength/strength);
            enemy.dead = true;
            return;
        }
        if(strength < enemy_strength) {
            cout << enemy.name << " defeats " << name << endl;
            enemy.strengthChange(strength/enemy_strength);
            dead = true;
            return;
        }
        
    }
    
    void display() const{
        cout << name << " has an army of " << army.size() << endl;
        for(const Warrior* i : army) {
            cout << '\t' << i->getName() << ": " << i->getStrength() << endl;
        }
    }
    
private:
    string name;
    vector<Warrior*> army;
    bool dead = false;
};

int main() {
    
    Noble art("King Arthur");
    Noble lance("Lancelot du Lac");
    Noble jim("Jim");
    Noble linus("Linus Torvalds");
    Noble billie("Bill Gates");
    
    Warrior cheetah("Tarzan", 10);
    Warrior wizard("Merlin", 15);
    Warrior theGovernator("Conan", 12);
    Warrior nimoy("Spock", 15);
    Warrior lawless("Xena", 20);
    Warrior mrGreen("Hulk", 8);
    Warrior dylan("Hercules", 3);
    
    jim.hire(nimoy);
    lance.hire(theGovernator);
    art.hire(wizard);
    lance.hire(dylan);
    linus.hire(lawless);
    billie.hire(mrGreen);
    art.hire(cheetah);
    
    jim.display();
    lance.display();
    art.display();
    linus.display();
    billie.display();
    
    art.fire(cheetah);
    art.display();
    
    art.battle(lance);
    jim.battle(lance);
    linus.battle(billie);
    billie.battle(lance);
    
}

