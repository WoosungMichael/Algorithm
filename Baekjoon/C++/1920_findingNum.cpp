#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> ft_sort(vector<int> &v){
    int tmp;
    int flag;
    for(int i = 0; i < v.size(); i++){
        flag = true;
        for(int j = 0; j < v.size() - 1 - i; j++){
            if(v[j] > v[j + 1]){
                tmp = v[j];
                v[j] = v[j + 1];
                v[j + 1] = tmp;
                flag = false;
            }
        }
        if(flag)
            return v;
    }
    return v;
}

void q_sort(vector<int> &v, int start, int end){
    if(start >= end)
        return;
    
    int pivot = start;
    int i = pivot + 1;
    int j = end;
    int tmp;

    while(i <= j){
        while(i <= end && v[i] <= v[pivot])
            i++;
        while(j > start && v[j] >= v[pivot])
            j--;
        
        if(i > j){ 
            tmp = v[j]; 
            v[j] = v[pivot]; 
            v[pivot] = tmp; 
        }
        else{ 
            tmp = v[i]; 
            v[i] = v[j]; 
            v[j] = tmp; 
        }
    }
    q_sort(v, start, j - 1); 
    q_sort(v, j + 1, end);

}

int main(){
    int N, M;
    int tmp;
    vector<int> v;

    ios_base::sync_with_stdio(0);cin.tie(0);
    cin >> N;
    for(int i = 0; i < N; i++){
        cin >> tmp;
        v.push_back(tmp);
    }
    cin >> M;

    sort(v.begin(), v.end());
    //ft_sort(v);
    //q_sort(v, 0, v.size() - 1);

    for(int i = 0; i < M; i++){
        cin >> tmp;
        bool flag = false;
        int left = 0;
        int right = N - 1;
        int mid;
        while(left <= right){
            mid = (left + right) / 2;
            if(tmp == v[mid]){
                flag = true;
                break;
            }
            else if(tmp > v[mid]){
                left = mid + 1;
            }
            else{
                right = mid - 1;
            }
        }
        if(flag)
            cout << "1\n";
        else
            cout << "0\n";
    }
}