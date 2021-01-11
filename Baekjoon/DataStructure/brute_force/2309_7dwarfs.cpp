#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	vector <int> v;
	int sum = 0;

	for (int i = 0; i < 9; i++) {
		int a;
		cin >> a;
		sum += a;
		v.push_back(a);
	}

	int flag = 0;
	for (int i = 0; i < v.size() - 1; i++) {
		for (int j = i+1; j < v.size(); j++) {
			if (v[i] + v[j] + 100 == sum) {
				v.erase(v.begin() + j);
				v.erase(v.begin() + i);
				flag = 1;
				break;
			}
		}
		if (flag == 1)
			break;
	}

	sort(v.begin(), v.end());

	for (int i = 0; i < v.size(); i++) {
		cout << v[i] <<'\n';
	}
}