#include <iostream>
#include <math.h>
using namespace std;

int main() {
	int n;
	int x1, y1, r1, x2, y2, r2;

	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> n;
	for (int i = 0; i < n; i++) {

		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;

		double d = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));

		int r_max;
		int r_min;
		if (r1 > r2) {
			r_max = r1;
			r_min = r2;
		}
		else {
			r_max = r2;
			r_min = r1;
		}

		if (d == 0)
			if (r1 == r2)
				cout << -1 << '\n';
			else
				cout << 0 << '\n';
		else
			if (d > r1 + r2)
				cout << 0 << '\n';
			else if (d == r1 + r2)
				cout << 1 << '\n';
			else {
				if (r_max > d + r_min)
					cout << 0 << '\n';
				else if (r_max == d + r_min)
					cout << 1 << '\n';
				else
					cout << 2 << '\n';
			}
	}

}