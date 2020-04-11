//
//  polynomial.cpp
//  hw08
//
//  Created by Kevin Xu on 12/8/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include "polynomial.hpp"
#include <iostream>
#include <vector>
using namespace std;
//constructor
Polynomial::Polynomial(const vector<int>& vc) {
    degree = int(vc.size()) - 1;
    for(size_t i = 0; i < vc.size() ; ++i) {
        headPtr = new Node(vc[i], headPtr);
    }
}
//copy constructor
Polynomial::Polynomial(const Polynomial& rhs) {
    degree = rhs.degree;
    Node* curr = rhs.headPtr;
    headPtr = new Node(curr->data);
    Node* tempHead = headPtr;
    while(curr->next) {
        tempHead->next = new Node(curr->next->data);
        tempHead = tempHead->next;
        curr = curr->next;
    }
}
//assignment operator
Polynomial& Polynomial::operator=(const Polynomial& rhs) {
    if(&rhs != this) {
        //free up
        Node* curr = headPtr;
        Node* next = headPtr->next;
        while(next) {
            delete curr;
            curr = next;
            next = next->next;
        }
        delete curr;
        //copy
        degree = rhs.degree;
        curr = rhs.headPtr;
        headPtr = new Node(curr->data);
        Node* tempHead = headPtr;
        while(curr->next) {
            tempHead->next = new Node(curr->next->data);
            tempHead = tempHead->next;
            curr = curr->next;
        }
    }
    return *this;
}
//destructor
Polynomial::~Polynomial() {
    Node* curr = headPtr;
    Node* next = headPtr->next;
    while(next) {
        delete curr;
        curr = next;
        next = next->next;
    }
    delete curr;
}
Polynomial& Polynomial::operator+=(const Polynomial& rhs) {
    *this = operator+(*this, rhs); //use the overloaded "+" operator (see below)
    return *this;
}
int Polynomial::evaluate(int x) const{
    int result = 0;
    int d = 0;
    Node* curr = headPtr;
    while(curr) {
        int power = 1;
        //calculate x to the power of d
        if(d > 0) {
            for(int i = 1; i <= d; ++i) {power *= x;}
        }
        result += power * curr->data;
        curr = curr->next;
        d++;
    }
    return result;
}
void Polynomial::display(Node* curr, int d, ostream& os) const{ //used in output operator to help display elements
    if(d > degree) return;
    display(curr->next, d+1, os);
    if(curr->data == 0 and degree != 0) return;
    if(d == 0) os << curr->data;
    else if(d == 1 && curr->data == 1) os << "x + ";
    else if(d == 1) os << curr->data << "x + ";
    else os << curr->data << "x^" << d << " + ";
}
ostream& operator<<(ostream& os, const Polynomial& rhs) {
    rhs.display(rhs.headPtr, 0, os);
    return os;
}
Polynomial operator+(const Polynomial& lhs, const Polynomial& rhs) {
    vector<int> vc;
    Node* lcurr = lhs.headPtr;
    Node* rcurr = rhs.headPtr;
    while(lcurr && rcurr) {
        vc.push_back(lcurr->data + rcurr->data);
        lcurr = lcurr->next;
        rcurr = rcurr->next;
    }
    while(lcurr) {
        vc.push_back(lcurr->data);
        lcurr = lcurr->next;
    }
    while(rcurr) {
        vc.push_back(rcurr->data);
        rcurr = rcurr->next;
    }
    while(vc.back() == 0 && vc.size() != 1) vc.pop_back(); //delete if the highest coefficient is zero
    int t;
    for(size_t i = 0; i < vc.size()/2; ++i) { //reverse the vector
        t = vc[i];
        vc[i] = vc[vc.size()-i-1];
        vc[vc.size()-i-1] = t;
    }
    return Polynomial(vc);
}
bool operator==(const Polynomial& lhs, const Polynomial& rhs) {
    if(lhs.degree != rhs.degree) return false;
    Node* lcurr = lhs.headPtr;
    Node* rcurr = rhs.headPtr;
    while(lcurr && rcurr) {
        if(lcurr->data != rcurr->data) return false;
        lcurr = lcurr->next;
        rcurr = rcurr->next;
    }
    return true;
}
bool operator!=(const Polynomial& lhs, const Polynomial& rhs) {return !(lhs == rhs);}

Node::Node(int data, Node* next) : data(data), next(next) {}
