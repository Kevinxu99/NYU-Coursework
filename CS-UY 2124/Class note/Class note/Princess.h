//
//  Princess.h
//  Class note
//
//  Created by Kevin Xu on 10/17/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#ifndef Princess_h
#define Princess_h

#include <string>
//Don't use "using namespace std;" in the header file
//namespace pollution
namespace Fantasy {
class FrogPrince;

class Princess {
public:
    Princess(const std::string& name);
    void display() const;
    void marries(FrogPrince& betrothed);
    
private:
    std::string name;
    FrogPrince* spouse;
};
    
}
#endif /* Princess_h */
