#include <iostream>
#include <string>
using namespace std;

void team6() {
    string s = "Welcome";
    if (s.find('Z') = string::npos) { // Syntax Error: Comparison should use ==
        cout << "Letter not found" << endl;
    }
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team6();
    return 0;
}
