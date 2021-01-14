#include <iostream>
using namespace std;

int main() {

    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int H, W, N;
        cin >> H >> W >> N;

        int a, b;
        if (N % H == 0) {
            a = H;
            b = N / H;
        }
        else {
            a = N % H;
            b = N / H + 1;
        }
        cout << a * 100 + b << endl;
    }
}