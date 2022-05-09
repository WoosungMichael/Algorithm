#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    vector<vector<int>> v;
    for(int i = 0; i < 4 * (n - 1) + 1; i++){
        vector<int> v2;
        for(int j = 0; j <= 2 * (n - 1); j++){
            v2.push_back(0);
        }
        v.push_back(v2);
    }

    int i = 0;
    int j = n - 1;
    int num = 1;
    v[i][j] = num;

    while(n - 1 > 0){
        for(int k = 0; k < n - 1; k++){
            i++;
            j++;
            num++;
            v[i][j] = num;
        }
        for(int k = 0; k < n - 1; k++){
            i += 2;
            num++;
            v[i][j] = num;
        }
        for(int k = 0; k < n - 1; k++){
            i++;
            j--;
            num++;
            v[i][j] = num;
        }
        for(int k = 0; k < n - 1; k++){
            i--;
            j--;
            num++;
            v[i][j] = num;
        }
        for(int k = 0; k < n - 1; k++){
            i -= 2;
            num++;
            v[i][j] = num;
        }
        for(int k = 0; k < n - 2; k++){
            i--;
            j++;
            num++;
            v[i][j] = num;
        }
        i++;
        j++;
        n--;
        num++;
        v[i][j] = num;
    }

    for(int i = 0; i < v.size(); i++){
        for(int j = 0; j < v[i].size(); j++){
            if(v[i][j] != 0)
                answer.push_back(v[i][j]);
        }
    }

    return answer;
}
