#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

class queue1 {
    Node* front;
    Node* rear;

public:
    queue1() : front(nullptr), rear(nullptr) {}

    void enqueue(int value){
        Node* newNode = new Node();
        newNode->data = value;
        newNode->next = NULL;

        if (rear == NULL) {
            front = rear = newNode;
        } else {
            rear->next = newNode;
            rear = newNode;
        }
    }

    void dequeue(){
        if(!front){
            cout << "Queue is empty, cannot dequeue." << endl;
            return;
        }
        Node* temp = front;
        front = front->next;
        if (front == NULL) {
            rear = NULL; // If the queue becomes empty after dequeue
        }
        delete temp;
    }

    void top(){
        if(!front){
            return;
        }
        cout << front->data << endl;
    }
    void isEmpty(){
        if(!front){
            cout << "Queue is empty" << endl;
        }
        else{
            cout << "Queue is not empty" << endl;
        }
    }
    void size(){
        int count = 0;
        Node* temp = front;
        while(temp){
            count++;
            temp = temp->next;
        }
        cout << "Size of the queue is: " << count << endl;
    }
};

int main() {
    queue1 q;
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    q.enqueue(4);
    q.enqueue(5);
    q.enqueue(6);
    q.enqueue(7);
    q.enqueue(8);
    q.enqueue(9);
    q.enqueue(10);

    q.top();
    q.size();
    q.isEmpty();

    q.dequeue();
    q.top();
    q.size();
    q.isEmpty();

    return 0;
}