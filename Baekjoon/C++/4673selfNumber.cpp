#include <iostream>
using namespace std;

int main() {
	int num[10001] = { 0, };

	for (int i = 1; i < 10001; i++) {
		if (num[i] == 1)
			continue;
		int j = i;
		while (j < 10001) {
			if (j < 10)
				j = j * 2;
			else if (10 <= j && j < 100)
				j = j + j / 10 + j % 10;
			else if (100 <= j && j < 1000)
				j = j + j / 100 + (j % 100) / 10 + j % 10;
			else if (1000 <= j && j < 10000)
				j = j + j / 1000 + (j % 1000) / 100 + (j % 1000 % 100) / 10 + j % 10;

			else if (j == 10000)
				break;

			if (j < 10001)
				num[j] = 1;
		}
	}

	for (int i = 1; i < 10001; i++) {
		if (num[i] == 0)
			cout << i << "\n";
	}
	cout << endl;
}