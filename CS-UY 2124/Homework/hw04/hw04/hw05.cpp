//
//  hw04.cpp
//  hw04
//
//  Created by Kevin Xu on 10/14/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

class Warrior {
public:
    Warrior(const string& name, const int strength) : name(name), strength(strength) {}
    
    const string& getName() const{
        return name;
    }
    
    int getStrength() const{
        return strength;
    }
    
    void changeStrength(double ratio) {//adjust strength according to the ratio
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
    
    const string& getName() const{
        return name;
    }
    
    bool hire(Warrior& someWarrior) {
        if(someWarrior.ifHired()) return false;
        if(dead) return false;
        someWarrior.getHired();
        army.push_back(&someWarrior);
        return true;
    }
    
    bool fire(Warrior& someWarrior) {
        if(dead) return false;
        bool foundWarrior = false; //check if the warrior is in the army of the noble
        for(size_t i = 0; i < army.size(); i++) {
            if(foundWarrior) army[i-1] = army[i];
            if(army[i] == &someWarrior) foundWarrior = true;
        }
        if(!foundWarrior) {
            cout << "Warrior is not in the army" << endl;
            return false;
        }
        army.pop_back();
        cout << someWarrior.getName() << ", you're fired! -- " << name << endl;
        someWarrior.getFired();
        return true;
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
            cout << "Mutual Annihalation: " << name << " and "
            << enemy.name << " die at each other's hands" << endl;
            dead = true;
            enemy.dead = true;
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
    
    int armyStrength() const{
        int combinedStrength = 0;
        for(const Warrior* i : army) {
            combinedStrength += i->getStrength();
        }
        return combinedStrength;
    }
    
    void strengthChange(double ratio) const{
        for(Warrior* i : army) {
            i->changeStrength(ratio);
        }
    }
};

//status command function
void status(const vector<Noble*>& nobles, const vector<Warrior*>& warriors) {
    cout << "Status" << endl;
    cout << "======" << endl;
    cout << "Nobles:" << endl;
    if(nobles.empty()) {//display nobles
        cout << "NONE" << endl;
    }
    else{
        for(Noble* i : nobles) {
            i->display();
        }
    }
    cout << "Unemployed Warriors:" << endl; //display unemployed warriors
    bool no_unemployed = true;
    for(Warrior* i : warriors) {
        if(!(i->ifHired())) {
            no_unemployed = false;
            cout << i->getName() << ": " << i->getStrength() << endl;
        }
    }
    if(no_unemployed) cout << "NONE" << endl;
}

void readCommand(const string& filename) { //execute all the command here
    ifstream ifs(filename);
    if(!ifs) {
        cerr << "Could not open the file." << endl;
        exit(1);
    }
    vector<Noble*> nobles;
    vector<Warrior*> warriors;
    string comd; //Command
    string name1, name2; //to store the names after the command
    int strength;
    while(ifs >> comd) {
        if(comd == "Noble") {
            ifs >> name1;
            bool if_exist = false; //check if a Noble already exists
            for(Noble* i : nobles) {
                if(i->getName() == name1) {
                    if_exist = true;
                    break;
                }
            }
            if(if_exist) {
                cout << "Noble already exists" << endl;
                continue;
            }
            nobles.push_back(new Noble(name1));
        }
        if(comd == "Warrior") {
            ifs >> name1 >> strength;
            bool if_exist = false; //check if a Warrior already exists
            for(Warrior* i : warriors) {
                if(i->getName() == name1) {
                    if_exist = true;
                    break;
                }
            }
            if(if_exist) {
                cout << "Warrior already exists" << endl;
                continue;
            }
            warriors.push_back(new Warrior(name1, strength));
        }
        if(comd == "Hire") {
            ifs >> name1 >> name2;
            bool if_noble = false; //check if the hirer(noble) exists
            bool if_warrior = false; //check if the warrior being hired exists
            for(Noble* i : nobles) {
                if(i->getName() == name1) {
                    if_noble = true;
                    for(Warrior* j : warriors) {
                        if(j->getName() == name2) {
                            if_warrior = true;
                            i->hire(*j);
                            break;
                        }
                    }
                    break;
                }
            }
            if(!if_noble) cout << "Noble doesn't exist" << endl;
            if(!if_warrior) cout << "Warrior doesn't exist" << endl;
        }
        if(comd == "Fire") {
            ifs >> name1 >> name2;
            bool if_noble = false;
            bool if_warrior = false;
            for(Noble* i : nobles) {
                if(i->getName() == name1) {
                    if_noble = true;
                    for(Warrior* j : warriors) {
                        if(j->getName() == name2) {
                            if_warrior = true;
                            i->fire(*j);
                            break;
                        }
                    }
                    break;
                }
            }
            if(!if_noble) cout << "Noble doesn't exist" << endl;
            if(!if_warrior) cout << "Warrior doesn't exist" << endl;
        }
        if(comd == "Battle") {
            ifs >> name1 >> name2;
            bool if_noble_1 = false; //check if the first noble exists
            bool if_noble_2 = false; //check if the second noble exists
            int ind1 = -1; //fist noble index
            int ind2 = -1; //second noble index
            for(size_t i=0; i < nobles.size(); ++i) {
                if(nobles[i]->getName() == name1) {
                    ind1 = int(i);
                    if_noble_1 = true;
                }
                if(nobles[i]->getName() == name2) {
                    ind2 = int(i);
                    if_noble_2 = true;
                }
            }
            if(!if_noble_1 || !if_noble_2) {
                cout << "One of the nobles doesn't exist" << endl;
                continue;
            }
            nobles[ind1]->battle(*nobles[ind2]);
        }
        if(comd == "Status") {
            status(nobles, warriors);
        }
        if(comd == "Clear") {
            for(Noble* i : nobles) {
                delete i;
            }
            nobles.clear();
            for(Warrior* i : warriors) {
                delete i;
            }
            warriors.clear();
        }
    }
    ifs.close();//close file
}

int main() {
    readCommand("nobleWarriors.txt");
}
