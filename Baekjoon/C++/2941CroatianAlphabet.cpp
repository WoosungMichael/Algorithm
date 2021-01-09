#include <iostream>
using namespace std;

int main() {
	string s;;
	cin >> s;

	int cnt = 0;
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == 'd' && s[i + 1] == 'z' && s[i + 2] == '=')
			cnt = cnt;
		else if (s[i + 1] == 'j' && (s[i] == 'l' || s[i] == 'n'))
			cnt = cnt;
		else if (s[i + 1] == '=' || s[i + 1] == '-')
			cnt = cnt;
		else
			cnt++;
	}
	cout << cnt;
}