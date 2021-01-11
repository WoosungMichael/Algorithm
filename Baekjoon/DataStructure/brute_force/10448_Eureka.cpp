#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;

		int flag = 0;
		for (int a = 1; a * (a + 1) / 2 < x; a++) {
			for (int b = 1; b * (b + 1) / 2 < x; b++) {
				for (int c = 1; c * (c + 1) / 2 < x; c++) {
					if (a * (a + 1) / 2 + b * (b + 1) / 2 + c * (c + 1) / 2 == x) {
						flag = 1;
						break;
					}
				}
				if (flag == 1)
					break;
			}
			if (flag == 1)
				break;
		}

		cout << flag << '\n';
	}
}