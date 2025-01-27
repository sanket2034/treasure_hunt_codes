#include <iostream>
using namespace std;

void team5() {
    int x = 5;
    for (int i = 0; i < x; i++) { // Logical Error: Should iterate 4 times
        cout << x + i << endl;
    }
    cout << "Sum: " << (x + i << endl; // Syntax Error: Missing closing parenthesis
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team5();
    return 0;
}
