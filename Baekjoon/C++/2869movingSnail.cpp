#include <iostream>
using namespace std;

int main() {

    int A, B, V;
    cin >> A >> B >> V;

    int day = 0;
    int height = 0;

    day = (V - A) / (A - B);

    if ((V - A) % (A - B) == 0)
        cout << day + 1;
    else
        cout << day + 2;
}