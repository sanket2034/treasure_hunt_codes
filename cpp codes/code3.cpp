#include <iostream>
using namespace std;

void team3() {
    int a = 5;
    int b == 10; // Syntax Error: Assignment uses single =
    if (a > b) { // Logical Error: Condition will always be false
        cout << "a is greater" << endl;
    }
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team3();
    return 0;
}
