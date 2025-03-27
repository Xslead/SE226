#include <iostream>
using namespace std;

double harmonic_number(int n) {
  if (n == 1) {
    return 1.0;
  }

  return harmonic_number(n - 1) + 1.0 / n;
}
double harmonic_number() {
  int n;
  cout << "Enter a positive integer n: ";
  cin >> n;

  if (n <= 0) {
    cout << "Please enter a positive integer." << endl;
    return 0.0;
  }

  return harmonic_number(n);
  }

int main() {
  int n;
  cout << "Enter a positive integer n: ";
  cin >> n;

  if (n <= 0) {
    cout << "Please enter a positive integer." << endl;
    return 1;
  }

  cout << "H(" << n << ") = " << harmonic_number(n) << endl;

  return 0;
}
