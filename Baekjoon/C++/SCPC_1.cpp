/*
You should use the standard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful.
*/

#include <iostream>
#include <vector>
using namespace std;

int Answer;

int main(int argc, char** argv)
{
	int T, test_case;
	/*
	   The freopen function below opens input.txt file in read only mode, and afterward,
	   the program will read from input.txt file instead of standard(keyboard) input.
	   To test your program, you may save input data in input.txt file,
	   and use freopen function to read from the file when using cin function.
	   You may remove the comment symbols(//) in the below statement and use it.
	   Use #include<cstdio> or #include <stdio.h> to use the function in your program.
	   But before submission, you must remove the freopen function or rewrite comment symbols(//).
	 */

	 // freopen("input.txt", "r", stdin);
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> T;
	for (test_case = 0; test_case < T; test_case++)
	{

		Answer = 0;
		/////////////////////////////////////////////////////////////////////////////////////////////
		int N;
		cin >> N;

		int p;
		vector <int> v1;
		vector <bool> v2;
		int i;
		for (i = 0; i < N; i++) {
			cin >> p;
			v1.push_back(p);
			v2.push_back(false);
		}

		for (i = 0; i < N; i++) {
			int j = i;
			if (v2[j] == false) {
				Answer++;
				v2[j] = true;
				while (j + v1[j] < N) {
					j = j + v1[j];
					if (v2[j] == true) {
						Answer--;
						break;
					}
					v2[j] = true;
				}
			}
		}
		/////////////////////////////////////////////////////////////////////////////////////////////

		 // Print the answer to standard output(screen).
		cout << "Case #" << test_case + 1 << endl;
		cout << Answer << endl;
	}

	return 0;//Your program should return 0 on normal termination.
}