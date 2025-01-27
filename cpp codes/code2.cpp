#include <iostream>
#include <vector>
using namespace std;

void team2() {
    vector<int> lst = {1, 2, 3, 4};
    for (int i = 0; i <= 4; i++) { // Logical Error: Out-of-range loop
        cout << lst.at(i) << endl; // Will cause runtime error
    }
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team2();
    return 0;
}
