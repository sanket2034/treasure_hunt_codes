#include <iostream>
using namespace std;

void team1() {
    int num = 10;
    if (num = 10) { // Syntax Error: Should use ==
        int result = num / 0; // Logical Error: Division by zero
        cout << "Result: " << result << endl;
    }
    else {
        cout << "You qualify for the next round!" << endl;
    }
}

int main() {
    team1();
    return 0;
}
