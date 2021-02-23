#include <string>
using namespace std;

bool solution(string s) {
    bool answer = true;

    if (s.length() != 4 && s.length() != 6)
        return false;

    for (int i = 0; i < s.length(); i++) {
        if (0 > (s[i] - '0') || (s[i] - '0') > 10)
            return false;
    }

    return answer;
}