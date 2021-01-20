#include <iostream>
using namespace std;

int main() {
    int M, N;
    cin >> M >> N;

    int* num = new int[N - M + 1];

    for (int i = 0; i < N - M + 1; i++) {
        num[i] = M + i;
    }

    for (int i = 2; i * i <= N; i++) {

        for (int j = 0; j < N - M + 1; j++) {
            if (num[j] == 0) {
                continue;
            }
            else {
                if (num[j] % i == 0) {
                    if (num[j] / i != 1) {
                        num[j] = 0;
                    }
                }
            }
        }
    }

    for (int i = 0; i < N - M + 1; i++) {
        if (num[i] != 0 && num[i] != 1) {
            cout << num[i] << '\n';
        }
    }
}