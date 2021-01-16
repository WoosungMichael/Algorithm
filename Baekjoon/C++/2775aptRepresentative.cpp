#include <iostream>
using namespace std;

int main() {

    int T;
    cin >> T;
    int apt[15][15];

    for (int i = 0; i < 15; i++) {
        apt[0][i] = i;
    }
    for (int i = 0; i < 15; i++) {
        apt[i][0] = 0;
        apt[i][1] = 1;
    }

    for (int i = 1; i < 15; i++) {
        for (int j = 1; j < 15; j++) {
            apt[i][j] = apt[i - 1][j] + apt[i][j - 1];
        }
    }

    for (int i = 0; i < T; i++) {
        int k, n;
        cin >> k >> n;

        cout << apt[k][n] << endl;
    }
}