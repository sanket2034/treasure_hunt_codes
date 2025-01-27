#include <iostream>
using namespace std;

void team14() {
    string num1 = "100";
    int num2 = 50;
    int total = num1 + num2; // Logical Error: Cannot add string and integer
    cout << "Total: " << total << endl;
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team14();
    return 0;
}
