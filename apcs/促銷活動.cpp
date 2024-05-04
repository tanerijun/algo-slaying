#include <iostream>
using namespace std;

void discount(double& p1, double& p2) {
    // Apply discount to the second item ONLY if they have the same price
    if (p1 == p2) {
        p2 = p2 / 2.0;
    }
}

int main() {
    double p1, p2;
    cout << "Original price:" << endl;
    cin >> p1 >> p2;
    
    discount(p1, p2);
    
    cout << "Price after discount:" << endl;
    cout << p1 << " " << p2 << endl;
    return 0;
}