#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	string line;
	cin >> line;

	vector<int>num(50, 0);
	int index = 0;

	bool isNum = false;
	for (int i = 0; i < line.length(); i++) {

		if (line[i] == '+') {
			isNum = false;
		}
		else if (line[i] == '-') {
			index++;
			isNum = false;
		}
		else {
			if (isNum == false) {
				num[index] += (stoi(&line[i]));
				isNum = true;
			}
		}
	}

	int ans = num[0];
	for (int i = 1; i < 50; i++) {
		ans -= num[i];
	}

	cout << ans;
}