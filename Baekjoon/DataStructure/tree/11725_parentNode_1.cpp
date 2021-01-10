#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); 
	cin.tie(NULL);
	vector<pair<int,int>> v;
	int n;
	cin >> n;
	v.push_back(make_pair(1, 1));
	
	for (int i = 0; i < n - 1; i++) {
		int a, b;
		cin >> a >> b;

		int flag = 0;
		for (int j = 0; j < v.size(); j++) {
			if (v[j].second == a) {
				flag = 1;
				v.push_back(make_pair(a, b));
				break;
			}
		}
		if(flag==0)
			v.push_back(make_pair(b, a));
	}

	for (int i = 2; i <= n; i++) {
		for (int j = 0; j < v.size(); j++) {
			if (v[j].second == i) {
				cout << v[j].first << '\n';
				break;
			}
		}
	}
}