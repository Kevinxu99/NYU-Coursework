//
//  linkedlist.cpp
//  Class note
//
//  Created by Kevin Xu on 11/14/18.
//  Copyright © 2018 Kevin Xu. All rights reserved.
//

#include <iostream>
using namespace std;

struct Node {
    Node(int data = 0, Node* next = nullptr) : data(data), next(next) {}
    int data;
    Node* next;
};

void listDisplay(const Node* headPtr) {
    while(headPtr != nullptr) {
        cout << headPtr->data << ' ';
        headPtr = headPtr->next;
    }
    cout << endl;
}

int listLength(Node* headPtr);

void listAddHead(Node*& headPtr, int data) {
    /*1.creating a node for the data
    Node* p = new Node(data);
    2.making the new node "point to" the old head
    p->next = headPtr;
    3.have the head pointer point to the new node
    headPtr = p*/
    headPtr = new Node(data, headPtr);
}

bool listRemoveHead(Node*& headPtr) {
    Node* second = headPtr->next;
    delete headPtr;
    headPtr = second;
}
