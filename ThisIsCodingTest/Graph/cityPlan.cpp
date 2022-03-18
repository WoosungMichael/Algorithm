#include <iostream>
#include <vector>
#include <algorithm>
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
    if(v[x] != x){
        v[x] = find_parent(v, v[x]);
    }
    return v[x];
}

bool cmp(vector<int> v1, vector<int> v2){
    return(v1[2] < v2[2]);
}

int main(){
    ios_base :: sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);
    
    int N, M;
    cin >> N >> M;

    int tmp;
    vector<vector<int>> v;
    for(int i = 0; i < M; i++){
        vector<int> v2;
        for(int j = 0; j < 3; j++){
            cin >> tmp;
            v2.push_back(tmp);
        }
        v.push_back(v2);
    }

    vector<int> parent;
    for(int i = 0; i <= N; i++){
        parent.push_back(i);
    }

    sort(v.begin(), v.end(), cmp);

    int cnt = 0;
    int a, b;
    for(int i = 0; i < v.size(); i++){
        a = find_parent(parent, v[i][0]);
        b = find_parent(parent, v[i][1]);
        if(a != b){
            if(a > b)
                parent[a] = b;
            else
                parent[b] = a;
            cnt += v[i][2];
            tmp = v[i][2];
        }
    }
    cnt -= tmp;
    cout << cnt;
}


// #include <iostream>
// #include <vector>
// #include <algorithm>
// using namespace std;

// int find_parent(vector<int> v, int x){
//     if(v[x] != x){
//         v[x] = find_parent(v, v[x]);
//     }
//     return v[x];
// }

// void unionParent(vector<int> &v, int a, int b) {
// 	a = find_parent(v, a);
// 	b = find_parent(v, b);

// 	if(a < b)
//         v[b] = a;
//     else
//         v[a] = b;
// }

// bool cmp(vector<int> v1, vector<int> v2){
//     return(v1[2] < v2[2]);
// }

// int main(){
//     ios_base :: sync_with_stdio(false); 
//     cin.tie(NULL); 
//     cout.tie(NULL);
    
//     int N, M;
//     cin >> N >> M;

//     int tmp;
//     int a, b, c;
//     vector<pair<int, pair<int, int>>> v;
//     for(int i = 0; i < M; i++){
//         cin >> a >> b >> c;
//         v.push_back({c, {a, b}});
//     }

//     vector<int> parent;
//     for(int i = 0; i <= N; i++){
//         parent.push_back(i);
//     }

//     sort(v.begin(), v.end());

//     int cnt = 0;
//     for(int i = 0; i < v.size(); i++){
//         a = find_parent(parent, v[i].second.first);
//         b = find_parent(parent, v[i].second.second);
//         if(a != b){
//             unionParent(parent, v[i].second.first, v[i].second.second);
//             cnt += v[i].first;
//             tmp = v[i].first;
//         }
//     }
//     cnt -= tmp;
//     cout << cnt;
// }
