#include <iostream>
using namespace std;

int main() {
	int turn = 1;

	while (1) {
		int L, P, V;
		cin >> L >> P >> V;

		if (L == 0 && P == 0 && V == 0)
			break;

		int cnt = 0;
		cnt += L * (V / P);

		if (V % P <= L)
			cnt += V % P;
		else
			cnt += L;

		cout << "Case " << turn << ": " << cnt << '\n';
		
		turn++;
	}
}