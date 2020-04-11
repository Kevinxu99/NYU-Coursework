//
//  hw01.cpp
//  hw01
//
//  Created by Kevin Xu on 9/24/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include <stdio.h>
#include <fstream>
#include <vector>
#include <iostream>
using namespace std;

struct Warrior {
    string name;
    int strength;
};

void new_Warrior(const string& name, const int strength, vector<Warrior>& warriors) { //Warrior
    Warrior war;
    war.name = name;
    war.strength = strength;
    warriors.push_back(war);
}

void battle(const string& name1, const string& name2, vector<Warrior>& warriors) { //Battle
    size_t ind1 = -1;
    size_t ind2 = -1;
    
    for(size_t i=0; i <= warriors.size(); ++i) { //find the indices of the two warriors that are battling
        if(warriors[i].name == name1) {
            ind1 = i;
        }
        if(warriors[i].name == name2) {
            ind2 = i;
        }
    }
    
    if(ind1 == -1 || ind2 == -1) return;
    
    cout<< name1 << " battles " << name2 << endl;
    
    if(warriors[ind1].strength == 0) {
        if(warriors[ind2].strength ==0) {
            cout<< "Oh, NO! They're both dead! Yuck!" << endl;
            return;
        }
        else {
            cout<<"He's dead, " << warriors[ind2].name << endl;
            return;
        }
    }
    
    if(warriors[ind2].strength == 0) {
        cout << "He's dead, " << warriors[ind1].name << endl;
        return;
    }
    
    if(warriors[ind1].strength > warriors[ind2].strength) {
        cout << warriors[ind1].name << " defeats " << warriors[ind2].name << endl;
        warriors[ind1].strength = warriors[ind1].strength - warriors[ind2].strength;
        warriors[ind2].strength = 0;
    }
    else if (warriors[ind2].strength > warriors[ind1].strength) {
        cout << warriors[ind2].name << " defeats " << warriors[ind1].name << endl;
        warriors[ind2].strength = warriors[ind2].strength - warriors[ind1].strength;
        warriors[ind1].strength = 0;
    }
    else {
        cout << "Mutual Annihilation: " << name1 << " and " << name2 << " die at each other's hands" << endl;
        warriors[ind1].strength = 0;
        warriors[ind2].strength = 0;
    }
    
}

void display_Warriors (const vector<Warrior>& warriors) {      //Status
    cout << "There are: " << warriors.size() << " warriors" << endl;
    for (const Warrior& w : warriors) {
        cout << "Warrior: " << w.name << ", strength: " << w.strength << endl;
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
    string name1, name2;
    int strength;
    while(ifs >> comd) {
        if(comd == "Warrior") {
            ifs >> name1 >> strength;
            new_Warrior(name1, strength, warriors);
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

