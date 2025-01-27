#include <iostream>
using namespace std;

void team20() {
    int a = 10;
    if (a = 10) { // Syntax Error: Assignment uses single =
        cout << "a is equal to 10" << endl;
    }
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team20();
    return 0;
}
