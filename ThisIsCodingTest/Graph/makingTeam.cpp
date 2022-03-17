#include <iostream>
#include <vector>
using namespace std;

int max(int a, int b){
    if(a > b)
        return a;
    else
        return b;
}

int min(int a, int b){
    if(a < b)
        return a;
    else
        return b;
}

int find_parent(vector<int> v, int x){
    if(v[x] != x)
        v[x] = find_parent(v, v[x]);
    return v[x];
}

int main(){
    int N, M;
    cin >> N >> M;

    vector<int> v;

    for(int i = 0; i <= N; i++){
        v.push_back(i);
    }

    int a, b, c;
    for(int i = 0; i < M; i++){
        cin >> a >> b >> c;
        if(a == 0)
            v[max(b, c)] = min(b, c);
        else{
            if(find_parent(v, b) == find_parent(v, c))
                cout << "YES" << endl;
            else
                cout << "NO" << endl;
        }
    }
}