#include <iostream>
#include <string>
using namespace std;

void team11() {
    string x = "15";
    int y = x + 5; // Logical Error: Cannot add string and integer
    cout << y << endl;
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team11();
    return 0;
}
