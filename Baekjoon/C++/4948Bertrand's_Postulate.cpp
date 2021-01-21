#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    while (1) {
        int n;
        cin >> n;

        int cnt = 0;
        if (n == 0)
            break;
        else {
            for (int i = n + 1; i <= 2 * n; i++) {
                int prime = 0;
                for (int j = 2; j * j <= i; j++) {
                    if (i % j == 0) {
                        prime = 1;
                        break;
                    }

                }
                if (prime == 0)
                    cnt++;
            }
            cout << cnt << '\n';
        }
    }
}
