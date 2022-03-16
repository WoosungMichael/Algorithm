#include <iostream>
#include <vector>
using namespace std;

int mix(int a, int b){
    if(a < b)
        return a;
    else
        return b;
}


void fw(vector<vector<int>> &v, int n){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            for(int k = 0; k < n; k++){
                v[j][k] = min(v[j][k], v[j][i] + v[i][k]);
            }
        }
    }
}

int main(){
    int N;
    cin >> N;

    vector<vector<int>> v;
    int tmp;

    for(int i = 0; i < N; i++){
        vector<int> v2;
        for(int j = 0; j < N; j++){
            cin >> tmp;    
            if(tmp == 0)
                v2.push_back(10001);
            else
                v2.push_back(tmp);
        }
        v.push_back(v2);
    }

    fw(v, N);

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(v[i][j] < 10001)
                cout << 1 << " ";
            else
                cout << 0 << " ";
        }
        cout << endl;
    }
}