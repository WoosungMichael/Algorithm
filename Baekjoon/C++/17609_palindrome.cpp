#include <iostream>
using namespace std;

int main(){
    int T;
    cin >> T;

    for(int i = 0; i < T; i++){
        string tmp;
        cin >> tmp;

        int flag = 0;
        int index = 0;
        int left = 0;
        int right = tmp.length() - 1;
        
        while(true){
            if(left >= right)
                break;
            if(flag == 0){
                if(tmp[left] == tmp[right]){
                    left++;
                    right--;
                }
                else{
                    flag = 1;
                    index = left;
                    right--;
                }
            }
            else if(flag == 1){
                if(tmp[left] == tmp[right]){
                    left++;
                    right--;
                }
                else{
                    flag = 2;
                    left = index + 1;
                    right = tmp.length() - 1 - index;
                }
            }
            else{
                if(tmp[left] == tmp[right]){
                    left++;
                    right--;
                }
                else{
                    flag = 3;
                    break;
                }
            }
        }
        if(flag == 0)
            cout << 0 << endl;
        else if(flag == 1 || flag == 2)
            cout << 1 << endl;
        else
            cout << 2 << endl;
    }
}

// int main(){
//     int T;
//     cin >> T;

//     for(int i = 0; i < T; i++){
//         string tmp;
//         cin >> tmp;
        
//         int left = 0;
//         int right = tmp.length() - 1;
//         int flag = 1;
//         int cnt1 = 0;
//         int cnt2 = 0;
//         while(left < right){
//             if(flag){
//                 if(tmp[left] == tmp[right]){
//                     left++;
//                     right--;
//                     cnt1 += 1;
//                     cnt2 += 1;
//                 }
//                 else{
//                     flag = 0;
//                 }
//             }
//             else{
//                 if(left + 1 <= right){
//                     if(tmp[left + 1] == tmp[right]){
//                         cnt1 += 1;
//                     }
//                     if(tmp[left] == tmp[right - 1]){
//                         cnt2 += 1;
//                     }
//                 }
//                 left++;
//                 right--;
//             }
//         }
//         if(tmp.length() % 2 == 0){
//             if(cnt1 == tmp.length() / 2 || cnt2 == tmp.length() / 2)
//                 cout << "0" << endl;
//             else if (cnt1 == tmp.length() / 2 - 1 || cnt2 == tmp.length() / 2 - 1)
//                 cout << "1" << endl;
//             else
//                 cout << "2" << endl;
//         }
//         else{
//             if(cnt1 == tmp.length() / 2 || cnt2 == tmp.length() / 2)
//                 cout << "0" << endl;
//             else if (cnt1 == tmp.length() / 2 - 1 || cnt2 == tmp.length() / 2 - 1)
//                 cout << "1" << endl;
//             else
//                 cout << "2" << endl;
//         }
//     }
// }