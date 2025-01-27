#include <iostream>
#include <vector>
using namespace std;

void team15() {
    vector<int> lst = {5, 10, 15};
    cout << lst[4] << endl; // Logical Error: Index out of range
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team15();
    return 0;
}
