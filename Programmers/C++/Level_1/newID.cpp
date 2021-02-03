#include <string>
#include <vector>

using namespace std;

string solution(string new_id) {
    string answer = "";
    string temp = "";

    string a = "";
    for (int i = 0; i < new_id.length(); i++) {
        if (65 <= new_id[i] && new_id[i] <= 90) {
            new_id[i] = tolower(new_id[i]);
            a += new_id[i];
        }
        else if (isdigit(new_id[i]) || (97 <= new_id[i] && new_id[i] <= 122) || new_id[i] == '-' || new_id[i] == '_' || new_id[i] == '.') {
            a += new_id[i];
        }
        else {
            temp += a;
            a = "";
        }
    }
    temp += a;

    string temp2 = "";
    temp2 += temp[0];
    for (int i = 1; i < temp.length(); i++) {
        if (temp[i - 1] == '.' && temp[i] == '.')
            continue;
        temp2 += temp[i];
    }

    string temp3 = "";
    if (temp2[0] == '.') {
        for (int i = 1; i < temp2.length() - 1; i++) {
            temp3 += temp2[i];
        }
        if (temp2[temp2.length() - 1] != '.')
            temp3 += temp2[temp2.length() - 1];
    }
    else {
        for (int i = 0; i < temp2.length() - 1; i++) {
            temp3 += temp2[i];
        }
        if (temp2[temp2.length() - 1] != '.')
            temp3 += temp2[temp2.length() - 1];
    }

    if (temp3.length() == 0)
        temp3 = "aaa";
    else if (temp3.length() <= 2) {
        while (1) {
            if (temp3.length() >= 3)
                break;
            temp3 += temp3[temp3.length() - 1];
        }
    }
    else if (temp3.length() > 15) {
        if (temp3[14] == '.')
            temp3 = temp3.substr(0, 14);
        else
            temp3 = temp3.substr(0, 15);
    }
    answer = temp3;
    return answer;
}