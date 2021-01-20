#include <iostream>
using namespace std;

int main() {
    int M, N;
    cin >> M >> N;

    int sum = 0;
    int min = 0;
    for (int i = N; i >= M; i--) {
        int prime = 0;
        for (int j = 1; j <= i; j++) {
            if (i % j == 0) {
                prime++;
            }
        }
        if (prime == 2) {
            sum += i;
            min = i;
        }
    }
    if (sum == 0)
        cout << -1 << "\n";
    else {
        cout << sum << "\n" << min << "\n";
    }
}
