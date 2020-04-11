//
//  Towers.cpp
//  Class note
//
//  Created by Kevin Xu on 12/5/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include <iostream>
using namespace std;

void towers(int n, char start, char target, char spare) {
    if(n > 0) {
        towers(n-1, start, spare, target);
        cout << "Move disk: " << n << " from spindle: " << start
        << "to spindle: " << target << endl;
        towers(n-1, spare, target, start);
    }
}

void printDigits(int n) {
    if(n == 0) return;
    printDigits(n/10);
    cout << n%10 << " ";
}

int main() {
    towers(64, 'A', 'C', 'B');
}
