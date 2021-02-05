#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	string line;
	cin >> line;

	vector<int>num(50,0);
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
				num[index] += (stoi(&line[i])); //***현재 인덱스 위치부터 시작하는 수 전체를 읽어옴***
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