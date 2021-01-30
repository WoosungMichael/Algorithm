#include <iostream>
using namespace std;

int main() {
	int x, y;
	cin >> x >> y;

	char** chess = new char* [x];
	for (int i = 0; i < x; i++) {
		chess[i] = new char[y];
	}

	for (int i = 0; i < x; i++) {
		for (int j = 0; j < y; j++) {
			cin >> chess[i][j];
		}
	}

	int min = 32;

	for (int i = 0; i < x - 7; i++) {
		for (int j = 0; j < y - 7; j++) {
			int cnt = 0;
			if (chess[i][j] == 'W') {
				for (int k = 0; k < 8; k++) {
					for (int l = 0; l < 8; l++) {
						if ((k + l) % 2 == 0) {
							if (chess[i + k][j + l] != 'W')
								cnt++;
						}
						else {
							if (chess[i + k][j + l] == 'W')
								cnt++;
						}
					}
				}
			}

			else {
				for (int k = 0; k < 8; k++) {
					for (int l = 0; l < 8; l++) {
						if ((k + l) % 2 == 0) {
							if (chess[i + k][j + l] != 'B')
								cnt++;
						}
						else {
							if (chess[i + k][j + l] == 'B')
								cnt++;
						}
					}
				}


			}
			if (cnt > 32)
				cnt = 64 - cnt;
			if (cnt < min)
				min = cnt;
		}
	}

	cout << min;

}