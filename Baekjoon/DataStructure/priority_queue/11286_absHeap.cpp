#include <iostream>
#include <queue>
#include <cstdlib>>
using namespace std;

struct comp {
	bool operator()(int a, int b){
		if (abs(a) != abs(b))
			return abs(a) > abs(b);
		else
			return a > b;
	}
};

int main() {
	int n;
	cin >> n;

	priority_queue <int, vector<int>, comp> pq;

	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;

		if (a != 0)
			pq.push(a);
		else {
			if (pq.empty())
				cout << 0 << '\n';
			else {
				cout << pq.top() << '\n';
				pq.pop();
			}
		}
	}


}