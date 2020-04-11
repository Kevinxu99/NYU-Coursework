//
//  FrogPrince.h
//  Class note
//
//  Created by Kevin Xu on 10/17/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#ifndef FrogPrince_h
#define FrogPrince_h

#include <string>

class Princess;

class FrogPrince {
public:
    FrogPrince(const std::string& name);
    void display() const;
    void setSpouse(Princess* pp);
private:
    std::string name;
    Princess* spouse;
};

#endif /* FrogPrince_h */
