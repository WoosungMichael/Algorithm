#include <iostream>
using namespace std;

int main() {
	int N, M;
	cin >> N >> M;

	int answer;
	if (N >= 3) {
		if (M >= 7) {
			answer = M - 2;
		}
		else if (M > 4) {
			answer = 4;
		}
		else {
			answer = M;
		}
	}
	else if (N == 2) {
		if ((M + 1) / 2 > 4)
			answer = 4;
		else
			answer = (M + 1) / 2;
	}
	else {
		answer = 1;
	}

	cout << answer;
}