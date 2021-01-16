#include <iostream>
#include <math.h>
using namespace std;

int main() {

    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int a, b;
        cin >> a >> b;
        int gap = b - a;
        int root_i = sqrt(gap);
        double root_d = sqrt(gap);
        if (root_i == root_d) {
            cout << 2 * root_i - 1 << endl;
        }
        else {
            if (gap <= root_i * (root_i + 1))
                cout << 2 * root_i << endl;
            else
                cout << 2 * root_i + 1 << endl;
        }
    }
}