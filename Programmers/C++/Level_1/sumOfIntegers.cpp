#include <string>

using namespace std;

long long solution(int a, int b) {
    long long answer = 0;
    answer = (a + b) * ((long long)abs(a - b) + 1) / 2;
    return answer;
}