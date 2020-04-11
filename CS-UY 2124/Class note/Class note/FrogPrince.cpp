//
//  FrogPrince.cpp
//  Class note
//
//  Created by Kevin Xu on 10/17/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include "FrogPrince.h"
#include "Princess.h"
#include <string>
#include <iostream>
using namespace std;

//FrogPrince Implementation Code
FrogPrince::FrogPrince(const string& name) : name(name) {}
void FrogPrince::display() const {cout << "Frog: " << name << endl;}
void FrogPrince::setSpouse(Princess* pp) {spouse = pp;}
