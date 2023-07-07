#include <vector>

using namespace std;

vector<int> move_zeroes(const vector<int> &input) {

    vector<int> withoutZeros;
    vector<int> justZeros;

    for (const int digit: input) {
        if (digit != 0) {
            withoutZeros.push_back(digit);
        } else {
            justZeros.push_back(digit);
        }
    }

    withoutZeros.insert(withoutZeros.end(), justZeros.begin(), justZeros.end());
    return withoutZeros;
}
