#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
    string answer = "";

    int index = -1;
    int len = number.length() - k;
    while (len--) {
        int max = 0;
        for (int i = index + 1; i < number.length() - len; i++) {
            if ((number[i] - '0') > max) {
                max = number[i] - '0';
                index = i;
            }
        }
        answer += to_string(max);
    }

    return answer;
}