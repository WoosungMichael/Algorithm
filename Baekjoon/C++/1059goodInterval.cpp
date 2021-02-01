#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int L;
	cin >> L;

	vector<int> v;
	for (int i = 0; i < L; i++) {
		int a;
		cin >> a;
		v.push_back(a);
	}
	int n;
	cin >> n;

	sort(v.begin(), v.end());
	if (n > v[v.size() - 1])
		v.push_back(1001);
	if (n < v[0])
		v.push_back(0);

	sort(v.begin(), v.end());

	int a = 0;
	int b = 0;
	for (int i = 0; i < v.size() - 1; i++) {
		if (v[i] < n && n < v[i + 1]) {
			a = v[i];
			b = v[i + 1];
			break;
		}
	}

	if (b - a <= 2)
		cout << 0 << '\n';
	else
		cout << (b - a - 1) * (b - a - 2) / 2 - (n - a - 1) * (n - a - 2) / 2 - (b - n - 1) * (b - n - 2) / 2 << "\n";

}