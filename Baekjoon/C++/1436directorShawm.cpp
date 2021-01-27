#include <iostream>
#include <string>
using namespace std;

int main() {
	int n;
	cin >> n;
	int cnt = 0;

	while (1) {
		for (int i = 666;; i++) {
			string num;
			num = to_string(i);
			for (int j = 0; j < num.length() - 2; j++) {
				if (num[j] == '6' && num[j + 1] == '6' && num[j + 2] == '6') {
					cnt++;
					break;
				}
			}
			if (cnt == n) {
				cout << i;
				return 0;
			}
		}
	}
}