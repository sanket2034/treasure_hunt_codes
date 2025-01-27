#include <iostream>
#include <vector>
using namespace std;

void team18() {
    vector<int> a = {10, 20, 30};
    vector<int> b = a + 5; // Logical Error: Cannot add a list and an integer
    for (int i = 0; i < b.size(); i++) {
        cout << b[i] << " ";
    }
    cout << endl;
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team18();
    return 0;
}
