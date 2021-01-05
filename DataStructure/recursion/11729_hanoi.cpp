#include <iostream>
using namespace std;

int cnt = 1;

void move(int n, int from, int to, int pass) {
	if (n == 1)
		cout << from << " " << to << "\n";
	else {
		move(n-1, from, pass, to);
		cout << from << " " << to << "\n";
		move(n-1, pass, to, from);
	}
}

int main() {
	cin.tie(NULL); 
	ios::sync_with_stdio(false);
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cnt *= 2;
	}
	cout << cnt - 1 << "\n";
	move(n, 1, 3, 2);

}