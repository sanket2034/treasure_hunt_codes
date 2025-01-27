#include <iostream>
#include <vector>
using namespace std;

void team17() {
    vector<int> x = {1, 2, 3};
    x[3] = 4; // Logical Error: Index out of range
    cout << x[0] << " " << x[1] << " " << x[2] << endl;
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team17();
    return 0;
}
