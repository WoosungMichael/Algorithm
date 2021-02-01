#include <iostream>
using namespace std;

int combination(int n, int m) {
	int answer = 1;
	for (int i = 1; i <= m; i++) {
		answer *= n--;
		answer /= i;
	}
	return answer;
}

int main() {
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		unsigned int N, M;
		cin >> N >> M;

		if(N > M) {
			cout << combination(N,M) << "\n";
		}
		else {
			cout << combination(M, N) << "\n";
		}
	}
}