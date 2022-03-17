#include <iostream>
#include <vector>
using namespace std;

int min(int a, int b){
    if(a < b)
        return a;
    else
        return b;
}

void fw(vector<vector<int>> &v, int n){
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            for(int k = 1; k <= n; k++){
                v[j][k] = min(v[j][k], v[j][i] + v[i][k]);
            }
        }
    }
}

int main(){
    int N, M, C;
    cin >> N >> M >> C;

    vector<vector<int>> v;
    for(int i = 0; i < N + 1; i++){
        vector<int> v2;
        for(int j = 0; j < N + 1; j++){
            v2.push_back(30000001);
        }
        v.push_back(v2);
    }

    int X, Y, Z;
    for(int i = 0; i < M; i++){
        cin >> X >> Y >> Z;
        v[X][Y] = Z;
    }

    fw(v, N);

    int num = 0;
    int max = 0;
    for(int i = 1; i <= N; i++){
        if(v[C][i] < 30000001 and v[C][i] >= 1){
            num += 1;
            if(max < v[C][i])
                max = v[C][i];
        }
    }

    cout << num << " " << max;
}