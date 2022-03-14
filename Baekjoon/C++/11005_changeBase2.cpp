#include <iostream>
using namespace std;

int main(){
    int a, b;
    cin >> a >> b;
    
    string str = "";
    string base = "0123456789";
    for(int i = 0; i < 26; i++){
        base += 'A' + i;
    }
    
    while(a >= b){
        str += base[a % b];
        a /= b;
    }
    str += base[a];

    for(int i = str.length() - 1; i >= 0; i--){
        cout << str[i];
    }
    cout << endl;
}