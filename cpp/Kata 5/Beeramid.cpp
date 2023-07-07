#include <cmath>

using namespace std;

int beeramid(int bonus, double price) {
    int i = 1;
    int counter = 0;
    double cost = 0;

    while (bonus - cost >= 0) {
        cost = cost + (pow(i, 2) * price);
        i++;
        counter++;
    }
    return bonus < 0 ? 0 : counter - 1;
}