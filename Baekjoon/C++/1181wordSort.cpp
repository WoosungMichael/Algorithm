#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool comp(string a, string b) {
	if (a.length() != b.length())
		return a.length() < b.length();
	else
		return a < b;
}

int main() {
	int n;
	cin >> n;

	vector<string> v;
	for (int i = 0; i < n; i++) {
		string str;
		cin >> str;
		v.push_back(str);
	}
	sort(v.begin(), v.end(), comp);
	v.erase(unique(v.begin(), v.end()), v.end());
	
	for (int i = 0; i < v.size(); i++) {
		cout << v[i] << "\n";
	}
}