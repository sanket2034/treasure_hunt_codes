#include <iostream>
using namespace std;

void team19() {
    int result = 100 / 0; // Logical Error: Division by zero
    cout << result << endl;
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team19();
    return 0;
}
