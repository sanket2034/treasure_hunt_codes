#include <iostream>
#include <vector>
using namespace std;

void team9() {
    vector<int> nums = {1, 2, 3, 4, 5};
    cout << nums(2) << endl; // Syntax Error: Incorrect indexing syntax, should use []
    int total = 0;
    for (int i = 0; i < nums.size(); i++) {
        total += nums[i];
    }
    total -= nums[nums.size() - 1]; // Logical Error: Incorrect total calculation
    cout << "Total: " << total << endl;
    cout << "You qualify for the next round!" << endl;
}

int main() {
    team9();
    return 0;
}
