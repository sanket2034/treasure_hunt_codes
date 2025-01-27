#include <iostream>
#include <vector>
using namespace std;

void team4() {
    vector<int> n = {1, 2, 3};
    cout << n(2) << endl; // Syntax Error: Incorrect indexing syntax, should use []
    if (n.size() > 5) { // Logical Error: Condition is unlikely to be true
        cout << "List is long!" << endl;
    }
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team4();
    return 0;
}
