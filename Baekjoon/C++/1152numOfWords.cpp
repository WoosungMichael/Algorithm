#include <iostream>
#include <string>
using namespace std;

int main() {
	string word;
	getline(cin, word);
	for (int i = 0; i < word.length(); i++) {
		word[i] = toupper(word[i]);
	}

	int cnt = 0;
	for (int i = 0; i < word.length(); i++) {
		if (65 <= word[i] && word[i] <= 90 && word[i + 1] == 32)
			cnt++;
	}

	if (word[word.length() - 1] == 32)
		cout << cnt;
	else
		cout << ++cnt;
}