#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;

	int a = 0;
	int b = 0;

	if (N == 4 || N == 7)
		cout << -1 << '\n';

	else {
		if (N % 5 == 0) {
			a = 0;
			b = N / 5;
		}
		else if (N % 5 == 1) {
			a = 2;
			b = N / 5 - 1;
		}
		else if (N % 5 == 2) {
			a = 4;
			b = N / 5 - 2;
		}
		else if (N % 5 == 3) {
			a = 1;
			b = N / 5;
		}
		else {
			a = 3;
			b = N / 5 - 1;
		}
		cout << a + b << '\n';
	}
}