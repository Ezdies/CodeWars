#include <string>
#include <algorithm>
#include <vector>

std::vector<std::string> permutations(std::string s) {

    std::vector<std::string> res;
    std::sort(s.begin(), s.end());

    do {
        res.push_back(s);
    } while (std::next_permutation(s.begin(), s.end()));

    return res;
}