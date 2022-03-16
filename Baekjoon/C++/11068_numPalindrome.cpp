#include <iostream>
using namespace std;

int main(){
    int T;
    cin >> T;

    for(int i = 0; i < T; i++){
        int num;
        cin >> num;

        int base = 2;
        int flag = 0;
        int tmp;
        int left, right;
        string str;
        while(base <= 64){
            tmp = num;
            str = "";
            while(tmp >= base){
                str += tmp % base;
                tmp /= base;
            }
            str += tmp;

            left = 0;
            right = str.length() - 1;
            int flag1 = 1;
            while(left < right){
                if(str[left] != str[right]){
                    flag1 = 0;
                }
                left++;
                right--;
            }
            if(flag1){
                flag = 1;
                break;
            }
            base++;
        }
        cout << flag << endl;
    }
}