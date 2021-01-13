#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n;
	cin >> n;

	vector <int> v;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		v.push_back(a);
	}

	sort(v.begin(), v.end());

	int sum = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n - i; j++) {
			sum += v[i];
		}
	}

	cout << sum;
}