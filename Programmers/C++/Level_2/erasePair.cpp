#include <iostream>
#include <vector>
using namespace std;

int solution(string s)
{
    int answer = 0;
    vector<int> v;

    v.push_back(s[0]);
    for (int i = 1; i < s.length(); i++) {
        if (s[i] == v[v.size() - 1]) {
            v.pop_back();
        }
        else {
            v.push_back(s[i]);
        }
    }

    if (v.size() == 0)
        answer = 1;

    return answer;
}