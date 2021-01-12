#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;

	int a = 1;
	int i;
	for (i=1; a < N; i++) {
		a += i * 6;
	}

	cout << i;
}