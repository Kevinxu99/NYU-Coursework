//
//  Noble.hpp
//  hw05
//
//  Created by Kevin Xu on 10/26/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#ifndef Noble_hpp
#define Noble_hpp

#include <iostream>
#include <string>
#include <vector>

namespace WarriorCraft{
    class Warrior;
    class Noble {
        friend std::ostream& operator<<(std::ostream& os, const Noble& rhs);
    public:
        Noble(const std::string& name);
        
        const std::string& getName() const;
        
        bool hire(Warrior& aWarrior);
        
        bool deleteWarrior(Warrior& aWarrior);
        
        bool fire(Warrior& aWarrior);
        
        void battle(Noble& enemy);
        
    private:
        std::string name;
        std::vector<Warrior*> army;
        bool dead = false;
        int armyStrength() const;
        void strengthChange(double ratio) const; //modify strength of Warrior
    };
}

#endif /* Noble_hpp */
