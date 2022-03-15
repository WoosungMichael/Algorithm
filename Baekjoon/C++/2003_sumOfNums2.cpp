#include <iostream>
#include <vector>
using namespace std;

int main(){
    int N, M;
    cin >> N >> M;
    vector<int> v;

    int tmp;
    for(int i = 0; i < N; i++){
        cin >> tmp;
        v.push_back(tmp);
    }

    int sum = 0;
    int cnt = 0;
    int left = 0;
    for(int i = 0; i < N; i++){
        sum += v[i];
        if(sum == M){
            cnt += 1;
            sum -= v[left];
            left += 1;
        }
        else if(sum > M){
            while(sum > M){
                sum -= v[left];   
                left += 1;            
            }
            if(sum == M){
                cnt += 1;
                sum -= v[left];
                left += 1;
            }
        }
    }
    cout << cnt;
}