#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> v;
int i, j, time, cnt, r, c, flag;

void init(int R, int C)
{
    r = R;
    c = C;
    for(i = 0; i < c; i++){
        vector<int> tmp;
        v.push_back(tmp);
    }
    time = 0;
}

int dropBlocks(int mTimestamp, int mCol, int mLen)
{
    cnt += mLen;

    vector<vector<int>> v2;
    for(i = 0; i < c; i++){
        vector<int> tmp;
        for(j = 0; j < v[i].size(); j++){
            v[i][j] += mTimestamp - time;
            if(v[i][j] >= r){
                cnt -= 1;
            }
            else{
                tmp.push_back(v[i][j]);
            }
        }
        v2.push_back(tmp);
    }
    time = mTimestamp;

    v = v2;

    for(i = 0; i < mLen; i++){
        v[mCol + i].push_back(0);
    }


    // cout << cnt << '\n';
    // for(i = 0; i < c; i++){
    //     int flag = 0;
    //     for(j = 0; j < v[i].size(); j++){
    //         cout << v[i][j] << " ";
    //         flag = 1;
    //     }
    //     if(flag)
    //         cout << "\n";
    // }
    // cout << "\n";
    return cnt;
}

int removeBlocks(int mTimestamp)
{
    vector<vector<int>> v2;
    for(i = 0; i < c; i++){
        vector<int> tmp;
        flag = 1;
        for(j = 0; j < v[i].size(); j++){
            v[i][j] += mTimestamp - time;
            if(v[i][j] >= r){
                cnt -= 1;
            }
            else{
                if(flag){
                    cnt -= 1;
                    flag = false;
                }
                else{
                    tmp.push_back(v[i][j]);
                }
            }

        }
        v2.push_back(tmp);
    }

    v = v2;
    time = mTimestamp;

    // cout << cnt << '\n';
    // for(i = 0; i < c; i++){
    //     for(j = 0; j < v[i].size(); j++){
    //         cout << v[i][j] << " ";
    //     }
    //     cout << "\n";
    // }
    // cout << "\n";
    return cnt;
}


#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>

void init(int R, int C);
int dropBlocks(int mTimestamp, int mCol, int mLen);
int removeBlocks(int mTimestamp);

#define CMD_INIT 100
#define CMD_DROP 200
#define CMD_REMOVE 300

static bool run()
{
    int query_num;
    scanf("%d", &query_num);

    int ret, ans;
    bool ok = false;

    for (int q = 0; q < query_num; q++)
    {
        int query;
        scanf("%d", &query);

        if (query == CMD_INIT)
        {
            int R, C;
            scanf("%d %d", &R, &C);
            init(R, C);
            ok = true;
        }
        else if (query == CMD_DROP)
        {
            int mTimestamp, mCol, mLen;
            scanf("%d %d %d", &mTimestamp, &mCol, &mLen);
            ret = dropBlocks(mTimestamp, mCol, mLen);
            scanf("%d", &ans);
            if (ans != ret)
            {
                ok = false;
            }
        }
        else if (query == CMD_REMOVE)
        {
            int mTimestamp;
            scanf("%d", &mTimestamp);
            ret = removeBlocks(mTimestamp);
            scanf("%d", &ans);
            if (ans != ret)
            {
                ok = false;
            }
        }

    }
    return ok;
}

int main()
{
    setbuf(stdout, NULL);
    // freopen("sample_input.txt", "r", stdin);
    int T, MARK;
    scanf("%d %d", &T, &MARK);

    for (int tc = 1; tc <= T; tc++)
    {
        int score = run() ? MARK : 0;
        printf("#%d %d\n", tc, score);
    }
    return 0;
}
