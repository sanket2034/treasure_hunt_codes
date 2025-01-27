#include <iostream>
using namespace std;

void team16() {
    int x = 0;
    if (x == "0") { // Logical Error: Type mismatch
        cout << "Zero as a string" << endl;
    }
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team16();
    return 0;
}
