#include <iostream>
using namespace std;

int main() {

	int A, B, C;
	cin >> A >> B >> C;

	int i = 0;
	if (B >= C)
		i = -1;
	else {
		i = A / (C - B) + 1;
	}
	cout << i;
}