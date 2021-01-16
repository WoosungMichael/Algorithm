#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	int* num = new int[N];
	for (int i = 0; i < N; i++)
		cin >> num[i];

	int count = 0;
	for (int i = 0; i < N; i++) {
		int cnt = 0;
		for (int j = 1; j <= num[i]; j++) {
			if (num[i] % j == 0)
				cnt++;
		}
		if (cnt == 2)
			count++;
	}

	cout << count;
}