//
//  Protector.hpp
//  hw06
//
//  Created by Kevin Xu on 11/11/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#ifndef Protector_hpp
#define Protector_hpp

#include <iostream>

namespace WarriorCraft {
    class Lord;
    
    class Protector {
    public:
        Protector(const std::string& name, int str);
        virtual void defend() const = 0;
        bool ifHired() const;
        void getHired(Lord& aLord);
        const std::string& getName() const;
        const std::string& getLordName() const;
        int getStrength() const;
        void change(double ratio);
        bool quit();
    private:
        std::string name;
        int strength;
        Lord* lord = nullptr;
    };
    
    class Warrior : public Protector {
    public:
        using Protector::Protector;
        virtual void defend() const = 0;
    };
    
    class Wizard : public Protector {
    public:
        using Protector::Protector;
        void defend() const;
    };
    
    class Archer : public Warrior {
    public:
        using Warrior::Warrior;
        void defend() const;
    };
    
    class Swordsman : public Warrior {
    public:
        using Warrior::Warrior;
        void defend() const;
    };
}

#endif /* Protector_hpp */
