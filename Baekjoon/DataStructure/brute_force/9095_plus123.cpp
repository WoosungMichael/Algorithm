#include <iostream>
using namespace std;

int factorial(int a) {
	if (a <= 1)
		return 1;
	else 
		return a * factorial(a - 1);
}

int main() {
	int n;
	cin >> n;

	for (int a = 0; a < n; a++) {
		int x;
		cin >> x;

		int cnt = 0;
		for (int i = 0; i <= x; i++) {
			for (int j = 0; i + j * 2 <= x; j++) {
				for (int k = 0; i + j * 2 + k * 3 <= x; k++) {
					if (i + j * 2 + k * 3 == x) {
						cnt += factorial(i + j + k) / (factorial(i) * factorial(j) * factorial(k));
					}
				}
			}
		}
		cout << cnt << '\n';
	}
}