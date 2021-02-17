#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n;
	cin >> n;

	int answer = 0;
	vector <int> v;
	int a;
	for (int i = 0; i < n; i++) {
		cin >> a;
		v.push_back(a);
	}

	for (int i = 0; i < n - 1; i++) {
		int min = v[i + 1];
		for (int j = i + 1; j < n; j++) {
			if (v[j] < min)
				min = v[j];
		}
		while (v[i] >= min) {
			v[i]--;
			answer++;
		}
	}

	int pre = v[0];
	int cnt = 0;
	for (int i = 1; i < n; i++) {
		if (pre == v[i]) {
			cnt++;
		}
		else {
			answer += cnt * (cnt + 1) / 2;
			cnt = 0;
		}
		pre = v[i];
	}

	cout << answer;
}