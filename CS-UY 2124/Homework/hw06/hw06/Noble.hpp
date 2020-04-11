//
//  Noble.hpp
//  hw06
//
//  Created by Kevin Xu on 11/11/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#ifndef Noble_hpp
#define Noble_hpp

#include <iostream>
#include <vector>

namespace WarriorCraft {
    class Protector;
    
    class Noble {
    public:
        Noble(const std::string& name);
        const std::string& getName() const;
        void battle(Noble& enemy);
        virtual void defense() const = 0;
        virtual int totalStrength() const= 0;
        virtual void strengthChange(double ratio) = 0;
    protected:
        bool ifDead() const;
    private:
        std::string name;
        bool dead = false;
    };
    
    class Lord : public Noble {
    public:
        using Noble::Noble;
        bool hires(Protector& pro);
        void delPro(const Protector* aPro);
    private:
        std::vector<Protector*> protectors;
        int totalStrength() const;
        void strengthChange(double ratio);
        void defense() const;
    };
    
    class PersonWithStrengthToFight : public Noble {
    public:
        PersonWithStrengthToFight(const std::string& name, int str);
    private:
        int strength;
        int totalStrength() const;
        void strengthChange(double ratio);
        void defense() const;
    };
}

#endif /* Noble_hpp */
