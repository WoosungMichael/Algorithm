#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	int n;
	cin >> n;

	int poss;
	int answer[3] = { -1,-1,-1 };
	vector<string> v;

	for (int i = 1; i <= 9; i++) {
		for (int j = 1; j <= 9; j++) {
			if (j == i)
				continue;
			for (int k = 1; k <= 9; k++) {
				if((k==i)||(k==j))
					continue;
				string s = to_string(i) + to_string(j) + to_string(k);
				v.push_back(s);
			}
		}
	}

	for (int i = 0; i < n; i++) {
		string num;
		int s, b;
		cin >> num >> s >> b;
		
		for (int i = v.size()-1; i >=0; i--) {
			int s_c = 0;
			int b_c = 0;
			for (int j = 0; j < 3; j++) {
				for (int k = 0; k < 3; k++) {
					if (v[i][j] == num[k]) {
						if (j == k) {
							s_c++;
							break;
						}
						else {
							b_c++;
							break;
						}
					}
				}
			}
			if ((s != s_c) || (b != b_c))
				v.erase(v.begin() + i);
		}
	}
	cout << v.size();
}