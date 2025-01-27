#include <iostream>
#include <vector>
using namespace std;

void team12() {
    vector<int> x = {1, 2, 3};
    cout << x.at(3) << endl; // Logical Error: Index out of range
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team12();
    return 0;
}
