#include <iostream>
#include <cmath>
#include <stdlib.h>
using namespace std;

int compare(const void* a, const void* b) {
	int num1 = *(int*)a;
	int num2 = *(int*)b;

	if (num1 < num2)
		return -1;
	if (num1 > num2)
		return 1;
	return 0;
}

int main() {
	int N;
	cin >> N;

	int* num = new int[N];
	for (int i = 0; i < N; i++) {
		cin >> num[i];
	}

	double avg;
	int mid;
	int most;
	int range;

	double sum = 0;
	for (int i = 0; i < N; i++) {
		sum += num[i];
	}
	avg = round(sum / N);

	qsort(num, N, sizeof(int), compare);

	mid = num[N / 2];

	int* count = new int[N];
	count[0] = 0;
	for (int i = 1; i < N; i++) {
		if (num[i] == num[i - 1])
			count[i] = count[i - 1] + 1;
		else
			count[i] = 0;
	}

	int max = 0;
	int index = 0;
	int index2 = 0;

	for (int i = 0; i < N; i++) {
		if (count[i] > max) {
			max = count[i];
			index = i;
		}
	}
	for (int i = 0; i < N; i++) {
		if ((count[i] == max) && (i != index)) {
			index2 = i;
			most = num[index2];
			break;
		}
		else
			most = num[index];
	}

	range = num[N - 1] - num[0];

	cout << avg << '\n' << mid << '\n' << most << '\n' << range << '\n';
}