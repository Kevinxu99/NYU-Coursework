//
//  Warrior.hpp
//  hw05
//
//  Created by Kevin Xu on 10/26/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#ifndef Warrior_hpp
#define Warrior_hpp

#include <iostream>
#include <string>

namespace WarriorCraft{
    class Noble;
    class Warrior {
        friend std::ostream& operator<<(std::ostream& os, const Warrior& warrior);
    public:
        Warrior(const std::string& name, const int strength);
        
        const std::string& getName() const;
        
        int getStrength() const;
        
        void changeStrength(double ratio);
        
        bool ifHired() const;
        
        void getHired(Noble& hirer);
        
        void getFired();
        
        void runaway();
    private:
        std::string name;
        int strength;
        Noble* theNoble = nullptr;
    };
}

#endif /* Warrior_hpp */
