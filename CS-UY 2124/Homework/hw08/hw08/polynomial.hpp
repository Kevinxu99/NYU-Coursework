//
//  polynomial.hpp
//  hw08
//
//  Created by Kevin Xu on 12/8/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#ifndef polynomial_hpp
#define polynomial_hpp

#include <iostream>
#include <vector>

struct Node {
    Node(int data = 0, Node* next = nullptr);
    int data;
    Node* next;
};

class Polynomial {
    friend std::ostream& operator<<(std::ostream& os, const Polynomial& rhs);
    friend Polynomial operator+(const Polynomial& lhs, const Polynomial& rhs);
    friend bool operator==(const Polynomial& lhs, const Polynomial& rhs);
    friend bool operator!=(const Polynomial& lhs, const Polynomial& rhs);
public:
    Polynomial(const std::vector<int>& vc = {0});
    Polynomial(const Polynomial& rhs);
    Polynomial& operator=(const Polynomial& rhs);
    ~Polynomial();
    Polynomial& operator+=(const Polynomial& rhs);
    int evaluate(int x) const;
private:
    int degree;
    Node* headPtr = nullptr;
    void display(Node* curr, int d, std::ostream& os) const;
};
#endif /* polynomial_hpp */
