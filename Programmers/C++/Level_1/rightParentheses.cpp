#include <string>
#include <vector>

using namespace std;

bool solution(string s)
{
    bool answer = true;

    vector <int> v;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '(')
            v.push_back(s[i]);
        else {
            if (v.size() != 0)
                v.pop_back();
            else
                return false;
        }
    }

    if (v.size() != 0)
        answer = false;

    return answer;
}