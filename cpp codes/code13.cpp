#include <iostream>
using namespace std;

void team13() {
    int a = 10, b = 20;
    if (a > b) { // Logical Error: Condition is False, but no handling
        cout << "a is greater" << endl;
    }
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team13();
    return 0;
}
