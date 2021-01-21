#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int num;
        cin >> num;

        int a = num / 2;
        int b;
        for (; a > 0; a--) {
            bool isPrime_a = true;
            for (int j = 2; j < a; j++) {
                if (a % j == 0) {
                    isPrime_a = false;
                    break;
                }
            }
            if (isPrime_a == false)
                continue;
            else {
                b = num - a;
                bool isPrime_b = true;
                for (int j = 2; j < b; j++) {
                    if (b % j == 0) {
                        isPrime_b = false;
                        break;
                    }
                }
                if (isPrime_b == false)
                    continue;
                else {
                    cout << a << " " << b << '\n';
                    break;
                }
            }
        }
    }
}