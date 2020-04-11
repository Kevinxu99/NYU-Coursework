//
//  hw02.cpp
//  hw02
//
//  Created by Kevin Xu on 9/30/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include <stdio.h>
#include <fstream>
#include <vector>
#include <iostream>
using namespace std;

class Warrior {
    friend ostream& operator<<(ostream& os, const Warrior& warrior) {
        os << "Warrior: " << warrior.name;
        return os;
    };
    class Weapon {
        friend ostream& operator<<(ostream& os, const Weapon& weapon) {
            os << weapon.weapon_name << ", " << weapon.strength;
            return os;
        };
    public:
        Weapon(const string& name, int strength) : weapon_name(name), strength(strength) {}
        int weapStrength() const {
            return strength;
        }
        void changeStrength(int new_Strength) {
            strength = new_Strength;
        }
    private:
        string weapon_name;
        int strength;
    };
    
public:
    Warrior(const string& name, const string& weapon_name, const int strength) : name(name), weapon(Weapon(weapon_name,strength)) {}
    void display(ostream& os) const {
        os << "Warrior: " << name << "," ;
    }
    bool check_name(const string& name1) {
        if(name == name1) return true;
        return false;
    }
    int weapon_strength() const{
        return weapon.weapStrength();
    }
    void changeStrength(int new_Strength) {
        weapon.changeStrength(new_Strength);
    }
    void display_Weapon() const{
        cout << weapon;
    }
private:
    string name;
    Weapon weapon;
};

void new_Warrior(const string& name, const string& weapon_name, const int strength, vector<Warrior>& warriors) { //Warrior
    Warrior war(name, weapon_name, strength);
    warriors.push_back(war);
}

void battle(const string& name1, const string& name2, vector<Warrior>& warriors) { //Battle
    size_t ind1 = -1;
    size_t ind2 = -1;
    
    for(size_t i=0; i <= warriors.size(); ++i) { //find the indices of the two warriors that are battling
        if(warriors[i].check_name(name1)) {
            ind1 = i;
        }
        if(warriors[i].check_name(name2)) {
            ind2 = i;
        }
    }
    
    if(ind1 == -1 || ind2 == -1) return;
    
    cout<< name1 << " battles " << name2 << endl;
    
    if(warriors[ind1].weapon_strength() == 0) {
        if(warriors[ind2].weapon_strength() ==0) {
            cout<< "Oh, NO! They're both dead! Yuck!" << endl;
            return;
        }
        else {
            cout<<"He's dead, " << name2 << endl;
            return;
        }
    }
    
    if(warriors[ind2].weapon_strength() == 0) {
        cout << "He's dead, " << name1 << endl;
        return;
    }
    
    if(warriors[ind1].weapon_strength() > warriors[ind2].weapon_strength()) {
        cout << name1 << " defeats " << name2 << endl;
        warriors[ind1].changeStrength(warriors[ind1].weapon_strength() - warriors[ind2].weapon_strength());
        warriors[ind2].changeStrength(0);
    }
    else if (warriors[ind1].weapon_strength() < warriors[ind2].weapon_strength()) {
        cout << name2 << " defeats " << name1 << endl;
        warriors[ind2].changeStrength(warriors[ind2].weapon_strength() - warriors[ind1].weapon_strength());
        warriors[ind2].changeStrength(0);
    }
    else {
        cout << "Mutual Annihilation: " << name1 << " and " << name2 << " die at each other's hands" << endl;
        warriors[ind1].changeStrength(0);
        warriors[ind2].changeStrength(0);
    }
    
}

void display_Warriors (const vector<Warrior>& warriors) {      //Status
    cout << "There are: " << warriors.size() << " warriors" << endl;
    for (const Warrior& w : warriors) {
        cout << w << ", weapon: ";
        w.display_Weapon();
        cout<<endl;
    }
}

int main() {
    ifstream ifs("warriors.txt");
    if (!ifs) {
        cerr << "Could not open the file.\n";
        exit(1);
    }
    vector<Warrior> warriors;   //vector that stores all the information about the warriors
    string comd;
    string weapon_name;
    string name1, name2;
    int strength;
    while(ifs >> comd) {
        if(comd == "Warrior") {
            ifs >> name1 >> weapon_name >> strength;
            new_Warrior(name1, weapon_name, strength, warriors);
        }
        if(comd == "Status") {
            display_Warriors(warriors);
        }
        if(comd == "Battle") {
            ifs >> name1 >> name2;
            battle(name1, name2, warriors);
        }
    }
}
