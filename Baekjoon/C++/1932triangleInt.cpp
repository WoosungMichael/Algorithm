#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n;
	cin >> n;

	vector <vector<int>> num;
	num.assign(n, vector<int>(n, 0));

	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= i; j++) {
			cin >> num[i][j];
		}
	}


	vector <vector<int>> sum;
	sum.assign(n, vector<int>(n, 0));

	for (int i = 0; i < n; i++) {
		for (int j = 0; j <= i; j++) {
			if (j == 0) {
				if (i == 0)
					sum[i][j] = num[i][j];
				else
					sum[i][j] = num[i][j] + sum[i - 1][j];

			}
			else {
				if (sum[i - 1][j - 1] > sum[i - 1][j])
					sum[i][j] = num[i][j] + sum[i - 1][j - 1];
				else
					sum[i][j] = num[i][j] + sum[i - 1][j];
			}
		}
	}

	int max = sum[n - 1][0];
	for (int i = 0; i < n; i++) {
		if (max < sum[n - 1][i])
			max = sum[n - 1][i];
	}
	cout << max;
}