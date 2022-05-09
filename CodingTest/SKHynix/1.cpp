#include <string>
#include <vector>

using namespace std;

bool check(vector<string> v, int r, int c, int len){
    if(v[r][c] == 'M'){
        for(int i = -2; i <= 2; i++){
            if((0 <= r + i && r + i < len && v[r + i][c] == 'C') || (0 <= c + i && c + i < len && v[r][c + i] == 'C'))
                return true;
        }
        if((r + 1 < len && c + 1 < len && v[r + 1][c + 1] == 'C') || (r + 1 < len && c - 1 >= 0 && v[r + 1][c - 1] == 'C') || (r - 1 >= 0 && c + 1 < len && v[r - 1][c + 1] == 'C') || (r - 1 >= 0 && c - 1 >= 0 && v[r - 1][c - 1] == 'C'))
            return true;
    }
    else if(v[r][c] == 'N'){
        for(int i = -3; i <= 3; i++){
            if((0 <= r + i && r + i < len && v[r + i][c] == 'C') || (0 <= c + i && c + i < len && v[r][c + i] == 'C'))
                return true;
        }
        for(int i = -2; i <= 2; i++){
            if((0 <= r + i && r + i < len && c - 1 >= 0 && v[r + i][c - 1] == 'C') || (0 <= r + i && r + i < len && c + 1 < len && v[r + i][c + 1] == 'C') || (0 <= c + i && c + i < len && r - 1 >= 0 && v[r - 1][c + i] == 'C') || (0 <= c + i && c + i < len && r + 1 < len && v[r + 1][c + i] == 'C'))
                return true;
        }
    }
    return false;
}

int solution(vector<string> seat) {
    int answer = 0;
    int len = seat.size();
    int i, j;
    for(i = 0; i < len; i++){
        for(j = 0; j < len; j++){
            if(check(seat, i, j, len))
                answer++;
        }
    }
    return answer;
}