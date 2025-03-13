#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class Stack {
private:
    Node* head;     // Points to top element of stack.
    int num;        // Number of elements (index-style tracking).
    int capacity;   // Fixed size limit (resized when full).

public:
    Stack(int initialCapacity) {  // You can set any initial size.
        head = nullptr;
        num = -1;
        capacity = initialCapacity;
    }

    void push(int x) {
        if (num >= capacity) {
            increaseCapacity();
        }
        Node* newNode = new Node(x);
        newNode->next = head;
        head = newNode;
        num++;
        cout << "Pushed " << x << endl;
    }

    int pop() {
        if (isEmpty()) {
            cout << "Stack is empty." << endl;
            return -1;
        }
        int poppedValue = head->data;
        head = head->next;
        num--;
        cout << "Popped " << poppedValue << endl;
        return poppedValue;
    }

    int peek() {
        if (isEmpty()) {
            cout << "Stack is empty." << endl;
            return -1;
        }
        cout << "Peeked " << head->data << endl;
        return head->data;
    }

    bool isEmpty() {
        return num < 0;
    }

    void increaseCapacity() {
        capacity *= 2;
    }

    bool deleteElement(int val) {
        if (isEmpty()) return false;

        Node* temp = head;
        Node* prev = nullptr;

        while (temp != nullptr) {
            if (temp->data == val) {
                if (prev == nullptr) {
                    head = temp->next;
                } else {
                    prev->next = temp->next;
                }
                delete temp;
                num--;
                return true;
            }
            prev = temp;
            temp = temp->next;
        }
        return false;
    }

    void seeStack() {
        if (isEmpty()) {
            cout << "Stack is empty." << endl;
            return;
        }

        cout << "Stack contents (top to bottom): ";
        Node* current = head;
        while (current != nullptr) {
            cout << current->data << " ";
            current = current->next;
        }
        cout << endl;
    }
};

int main() {
    // Create a stack with capacity of 5
    Stack myStack(5);

    // Test if stack is empty
    cout << "Is stack empty? " << (myStack.isEmpty() ? "Yes" : "No") << endl;

    // Add some elements
    myStack.push(10);
    myStack.push(20);
    myStack.push(30);

    // Display the stack
    myStack.seeStack();

    // Check top element
    myStack.peek();

    // Remove top element
    myStack.pop();

    // See updated stack
    myStack.seeStack();

    // Add more elements to test capacity increase
    myStack.push(40);
    myStack.push(50);
    myStack.push(60);  // This should trigger capacity increase

    // See final stack
    myStack.seeStack();

    // Test deleteElement
    cout << "Deleting element 40: ";
    if (myStack.deleteElement(40)) {
        cout << "Success!" << endl;
    } else {
        cout << "Failed!" << endl;
    }

    // See stack after deletion
    myStack.seeStack();

    return 0;
}