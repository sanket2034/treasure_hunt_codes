#include <iostream>
using namespace std;

void team10() {
    for (int i = 0; i < 5; i++) // Syntax Error: Missing braces
        cout << i << endl;
    int result = 10 / 0; // Logical Error: Division by zero
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team10();
    return 0;
}
