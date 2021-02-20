#include <iostream>
using namespace std;

int main() {
	int A, B;
	cin >> A >> B;

	int cnt = 0;
	while (A < B) {
		if (B % 2 != 0 && B % 10 != 1) {
			cout << "-1";
			return 0;
		}
		else if (B % 10 == 1) {
			B = B / 10;
			cnt++;
		}
		else {
			B = B / 2;
			cnt++;
		}
	}
	
	if (A == B)
		cout << cnt + 1;
	else
		cout << "-1";
}