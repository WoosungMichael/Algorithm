#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n;
	int total;
	cin >> n >> total;

	vector <int> v;

	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		v.push_back(a);
	}

	int num;
	for (num = 0; total != 0; num++) {
		for (int j = v.size() - 1; j >= 0; j--) {
			if (total - v[j] >= 0) {
				total -= v[j];
				break;
			}
		}
	}

	cout << num;
}