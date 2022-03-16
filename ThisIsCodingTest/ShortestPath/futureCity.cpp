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
    int N, M;
    int a, b;
    int X, K;
    
    cin >> N >> M;

    vector<vector<int>> v;
    for(int i = 0; i < N + 1; i++){
        vector<int> v2;
        for(int j = 0; j < N + 1; j++){
            if(i == j)
                v2.push_back(0);
            else
                v2.push_back(1000);
        }
        v.push_back(v2);
    }
    
    for(int i = 0; i < M; i++){
        cin >> a >> b;
        v[a][b] = 1;
        v[b][a] = 1;
    }

    fw(v, N);

    cin >> X >> K;

    if(v[1][K] + v[K][X] >= 1000)
        cout << "-1";
    else
    cout << v[1][K] + v[K][X];
}