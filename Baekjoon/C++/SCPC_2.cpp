/*
You should use the standard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful.
*/

#include <iostream>
#include <vector>
#include <string>
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
		int n, t;
		cin >> n >> t;
		
		char* arr1 = new char[n];
		cin >> arr1;

		int i;
		int* arr2 = new int[n];		
		for (i = 0; i < n; i++) {
			arr2[i] = 2;
		}

		for (i = 0; i < n; i++) {
			if (arr1[i] == '0') {
				if (i - t >= 0) {
					arr2[i - t] = 0;
				}
				if (i + t < n) {
					arr2[i + t] = 0;
				}
			}
		}

		for (i = 0; i < n; i++) {
			bool flag = true;
			if (arr1[i] == '1') {
				if (i - t >= 0) {
					if (arr2[i - t] != 1) {
						if (i + t < n and arr2[i + t] == 0) {
							if (arr2[i - t] != 0) {
								arr2[i - t] = 1;
							}
						}
						else {
							arr2[i - t] = 0;
						}
					}
					else {
						flag = false;
					}
				}
				if (i + t < n) {
					if (flag) {
						if (arr2[i + t] != 0) {
							arr2[i + t] = 1;
						}
					}
					else {
						arr2[i + t] = 0;
					}
				}
			}
		}
		
		for (i = 0; i < n; i++) {
			Answer = 10 * Answer + arr2[i];
		}

		/////////////////////////////////////////////////////////////////////////////////////////////

		 // Print the answer to standard output(screen).
		cout << "Case #" << test_case + 1 << endl;
		cout.fill('0');
		cout.width(n);
		cout << Answer << endl;
	}

	return 0;//Your program should return 0 on normal termination.
}