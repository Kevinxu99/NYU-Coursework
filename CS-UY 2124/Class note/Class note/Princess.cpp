//
//  Princess.cpp
//  Class note
//
//  Created by Kevin Xu on 10/17/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include "Princess.h"
#include "FrogPrince.h"
#include <iostream>
#include <string>
using namespace std;

void Princess::marries(FrogPrince& betrothed) {
    spouse = &betrothed;
    betrothed.setSpouse(this);
}

void Princess::display() const {cout << "Princess: " << name << endl;}

Princess::Princess(const string& name) : name(name) {}
