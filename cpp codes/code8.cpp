#include <iostream>
using namespace std;

void team8() {
    int a = 25;
    if (a % 2 == 1) {
        cout << "Even number" << endl; // Logical Error: Incorrect description
    }
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team8();
    return 0;
}
