#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int N;

bool comp(string a, string b) {
    return a[N] < b[N];
}

vector<string> solution(vector<string> strings, int n) {
    vector<string> answer;
    N = n;
    sort(strings.begin(), strings.end());
    stable_sort(strings.begin(), strings.end(), comp);
    answer = strings;
    return strings;
}