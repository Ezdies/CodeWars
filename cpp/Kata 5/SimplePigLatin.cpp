#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

string pig_it(string str) {

    istringstream iss(str);
    vector<string> words;
    for (string s; iss >> s;) {
        words.push_back(s);
    }
    auto result = std::string();

    for (const string &word: words) {
        if (word != "!" && word != "?" && word != "." && word != ",") {
            result += word.substr(1) + word.substr(0, 1) + "ay";
            result += " ";
        } else {
            result += word;
            result += " ";
        }
    }

    auto start = result.find_first_not_of(' ');
    auto end = result.find_last_not_of(' ');

    return result.substr(start, (end - start) + 1);
}