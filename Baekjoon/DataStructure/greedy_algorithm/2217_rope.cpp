#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n;
	cin >> n;

	vector<int> v;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		v.push_back(a);
	}

	sort(v.begin(), v.end());

	int max = v[0] * n;

	for (int i = 0; i < n; i++) {
		if (v[i] * (n - i) > max)
			max = v[i] * (n - i);
	}

	cout << max;
}