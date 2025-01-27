#include <iostream>
#include <vector>
using namespace std;

void team7() {
    vector<int> nums = {10, 20, 30};
    cout << nums.at(3) << endl; // Logical Error: Index out of range
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team7();
    return 0;
}
