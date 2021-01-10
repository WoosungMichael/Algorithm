#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	int group = 0;

	for (int i = 0; i < N; i++) {
		string word;
		cin >> word;
		int cnt = 0;

		for (int i = 0; i < word.length() - 1; i++) {
			if (word[i] == word[i + 1])
				continue;

			for (int j = i + 1; j < word.length(); j++) {
				if (word[i] == word[j]) 
					cnt++;	
			}
		}
		if (cnt == 0)
			group++;
	}

	cout << group;
}
