#include <iostream>
using namespace std;

int main(){
    string str;
    cin >> str;

    int i = 0;
    int cnt = 0;
    int flag = 1;
    while(i < str.length()){
        if(str[i] == '1'){
            i++;
            while(str[i] == '0'){
                cnt += 1;
                i++;
            }
            if(cnt < 2){
                flag = 0;
                break;
            }
            cnt = 0;
            while(str[i] == '1'){
                cnt += 1;
                i++;
            }
            if(cnt < 1){
                flag = 0;
                break;
            }
            if(cnt >= 2 && str[i] == '0' && str[i + 1] == '0')
                i--;
        }
        else{
            if(str[i + 1] == '1')
                i += 2;
            else{
                flag = 0;
                break;
            }
        }
    }

    if(flag)
        cout << "SUBMARINE";
    else
        cout << "NOISE";
}