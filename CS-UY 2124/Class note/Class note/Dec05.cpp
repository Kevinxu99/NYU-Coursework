//
//  Dec05.cpp
//  Class note
//
//  Created by Kevin Xu on 12/5/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    
    char array[] = "Bjarne Stroustrup";
    int len = 17;
    sort(array, array+len);
    
    vector<char> vc(array, array+len);
    // list<char> lc(vc[0]
    list<char> lc(vc.begin(), vc.end());
    
    //list<char>::iterator whereInList = myfind(lc.begin(), lc.end(), 'S')
    auto whereInList = myfind(lc.begin(), lc.end(), 'S');
    int target = 3;
    myfind_if(v1.begin(), v1.end(), [target] (int n) -> bool {return n%target == 0;}) //capture target
    myfind_if(v1.begin(), v1.end(), [&target] (int n) -> bool {return n%target == 0;}) //change target
    
    [] {} () //simplest
}
