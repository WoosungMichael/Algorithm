#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer;
    vector<string> v;
    string s = words[0];
    v.push_back(s);

    for (int i = 1; i < words.size(); i++) {

        if (s[s.length() - 1] == words[i][0]) {
            if (find(v.begin(), v.end(), words[i]) == v.end()) {
                v.push_back(words[i]);
                s = words[i];
            }
            else {
                answer.push_back(i % n + 1);
                answer.push_back(i / n + 1);
                break;
            }
        }
        else {
            answer.push_back(i % n + 1);
            answer.push_back(i / n + 1);
            break;
        }
    }
    if (answer.size() == 0) {
        answer.push_back(0);
        answer.push_back(0);
    }
    return answer;
}