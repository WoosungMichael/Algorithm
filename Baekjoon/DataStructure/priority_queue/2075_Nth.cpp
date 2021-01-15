#include <iostream>
#include <queue>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n;
	cin >> n;

	priority_queue <int, vector<int>, greater<int>> pq;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		pq.push(a);
	}

	for (int i = 0; i < n - 1; i++) {
		for (int j = 0; j < n; j++) {
			int a;
			cin >> a;
			pq.push(a);
		}
		for (int j = 0; j < n; j++) {
			pq.pop();
		}
	}

	cout << pq.top();

}