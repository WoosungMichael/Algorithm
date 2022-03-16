#include <iostream>
using namespace std;

int main(){
    int T;
    cin >> T;

    long long a, b;
    string str;
    long long left, right;
    for(int i = 0; i < T; i++){
        cin >> a >> b;
        str = "";
        while(a >= b){
            str += a % b;
            a /= b;
        }
        str += a;
        
        left = 0;
        right = str.length() - 1;
        int flag = 1;
        while(left < right){
            if(str[left] != str[right]){
                flag = 0;
                break;
            }
            left++;
            right--;
        }
        cout << flag << endl;
    }
}