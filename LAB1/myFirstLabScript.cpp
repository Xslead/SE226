#include <iostream>
using namespace std;

void q1() {
    cout << "What is your name?" << endl;
    string name;
    cin >> name;
    cout << "Hello " << name << endl;
    cout << "What is your id?" << endl;
    int id;
    cin >> id;
    cout << "Your ID is " << id << endl;
}
void q2() {
    cout << "Var1" << endl;
    int var1;
    cin >> var1;
    cout << "Var2" << endl;
    int var2;
    cin >> var2;

    float sum = var1 + var2;
    cout << "Sum is " << sum << endl;
    float diff = var1 - var2;
    cout << "Diff is " << diff << endl;
    float product = var1 * var2;
    cout << "Product is " << product << endl;

}
void q3() {
    cout << "Name " << endl;
    string name;
    cin >> name;
    cout << "Lab " << endl;
    float lab;
    cin >> lab;
    cout << "Midterm " << endl;
    float midterm;
    cin >> midterm;
    cout << "Final " << endl;
    float final;
    cin >> final;
    float lastScore = lab*25/100 + midterm*35/100 + final*40/100;
    cout << "Last score is " << lastScore << endl;
}


int q4(){
    cout<<"*\n**\n***\n**\n*";
    return 0;
}

int main() {
    q1();
    q2();
    q3();
    q4();
    return 0;

}