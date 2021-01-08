#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	int a, b, c;
	int cnt = 0;
	
	if (N < 100) {
		cnt += N;
	}
	else{
		cnt += 99;
		for (int i = 100; i <= N; i++) {
			a = i / 100;
			b = (i - a * 100) / 10;
			c = i % 10;
			if (b - a == c - b)
				cnt++;
		}
	}
	cout << cnt;
}
