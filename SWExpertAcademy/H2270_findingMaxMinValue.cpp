#include <iostream>
#include <vector>
using namespace std;
#define MAX_N 200001
#define rint register int
#define FAST __attribute((optimize("Ofast")))
int cnt, i, flag1, flag2;
int minV, maxV;

int v[MAX_N];
int min_v[MAX_N];
int max_v[MAX_N];

void init(int N, int mValue[])
{
    minV = 100000000;
    maxV = 0;
    cnt = N;
    for(i = 0; i < cnt; i++){
        v[i] = min_v[i] = max_v[i] = mValue[i];
    }
    for(i = cnt - 1; i >= 0; i--){
        if(v[i] < minV){
            minV = v[i];
        }
        if(v[i] > maxV){
            maxV = v[i];
        }
        min_v[i] = minV;
        max_v[i] = maxV;
    }
}
void add(int M, int mValue[])
{
    minV = 100000000;
    maxV = 0;
    for(i = 0; i < M; i++){
        v[cnt + i] = min_v[cnt + i] = max_v[cnt + i] = mValue[i];
    }
    cnt += M;
    
    for(i = cnt - 1; i > cnt - 1 - M; i--){
        if(v[i] < minV){
            minV = v[i];
        }
        if(v[i] > maxV){
            maxV = v[i];
        }
        min_v[i] = minV;
        max_v[i] = maxV;
    }

    for(i = cnt - 1 - M; i >= 0; i --){
        flag1 = 1;
        flag2 = 1;
        if(min_v[i] > minV){
            min_v[i] = minV;
            flag1 = 0;
        }
        if(max_v[i] < maxV){
            max_v[i] = maxV;
            flag2 = 0;
        }
        if(flag1 && flag2){
            break;
        }
    }
}
void erase(int mFrom, int mTo)
{
    if(mTo == cnt){
        minV = v[mFrom - 2];
        maxV = v[mFrom - 2];
    }
    else{
        minV = min_v[mTo];
        maxV = max_v[mTo];

        for(i = 0; i < cnt - mTo; i++){
            v[mFrom - 1 + i] = v[mTo + i];
            min_v[mFrom - 1 + i] = min_v[mTo + i];
            max_v[mFrom - 1 + i] = max_v[mTo + i];
        }
    }

    for(i = mFrom - 2; i >= 0; i--){
        flag1 = 1;
        flag2 = 1;
        if(v[i] < minV){
            min_v[i] = v[i];
            minV = v[i];
        }
        else{
            min_v[i] = minV;
            flag1 = 0;
        }
        if(v[i] > maxV){
            max_v[i] = v[i];
            maxV = v[i];
        }
        else{
            max_v[i] = maxV;
            flag2 = 0;
        }
        if(flag1 && flag2){
            break;
        }
    }

    cnt -= (mTo - mFrom + 1);
}
int find(int K)
{
	return max_v[cnt - K] - min_v[cnt - K];
}





#define MAX_ARR_SIZE (100000)
static int arr[MAX_ARR_SIZE];
static int N, M;
static int from, to;

int main(){
    int query_num;
    scanf("%d", &query_num);

    int ret, ans;
    bool ok = false;

    for (int q = 0; q < query_num; q++)
    {
        int query;
        scanf("%d", &query);

        if (query == 100)
        {
            scanf("%d", &N);
            for (int i = 0; i < N; i++){
                scanf("%d", &arr[i]);
            }
            init(N, arr);
            ok = true;
        }
        else if (query == 200)
        {
            scanf("%d", &M);
            for (int i = 0; i < M; i++)
                scanf("%d", &arr[i]);
            add(M, arr);
        }
        else if (query == 300)
        {
            scanf("%d%d", &from, &to);
            erase(from, to);

        }
        else if (query == 400)
        {
            int K;
            scanf("%d", &K);
            ret = find(K);
            scanf("%d", &ans);

            if (ans != ret)
                ok = false;
        }
    }
    return ok;
}
