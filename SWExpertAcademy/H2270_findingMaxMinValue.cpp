#include <iostream>

#include <vector>
using namespace std;
#define MAX_N 200001

int cnt, i, flag1, flag2;
int minV, maxV;

vector<int> v;
vector<int> min_v;
vector<int> max_v;

void init(int N, int mValue[])
{
    minV = 100000000;
    maxV = 0;
    cnt = N;
    for(i = 0; i < cnt; i++){
        v.push_back(mValue[i]);
        min_v.push_back(0);
        max_v.push_back(0);
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
        v.push_back(mValue[i]);
        min_v.push_back(0);
        max_v.push_back(0);
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
    if(mFrom == 1){
        v.erase(v.begin() + mFrom - 1, v.begin() + mTo);
        min_v.erase(min_v.begin() + mFrom - 1, min_v.begin() + mTo);
        max_v.erase(max_v.begin() + mFrom - 1, max_v.begin() + mTo);
    }
    else if(mTo == cnt){
        minV = v[mFrom - 2];
        maxV = v[mFrom - 2];

        v.erase(v.begin() + mFrom - 1, v.begin() + mTo);
        min_v.erase(min_v.begin() + mFrom - 1, min_v.begin() + mTo);
        max_v.erase(max_v.begin() + mFrom - 1, max_v.begin() + mTo);

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
    }
    else{
        minV = min_v[mTo];
        maxV = max_v[mTo];

        v.erase(v.begin() + mFrom - 1, v.begin() + mTo);
        min_v.erase(min_v.begin() + mFrom - 1, min_v.begin() + mTo);
        max_v.erase(max_v.begin() + mFrom - 1, max_v.begin() + mTo);

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
    cout << "\n\n";
    cout << cnt << "\n";
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << ' ';
    }
    cout << "\n";
    for(int i = 0; i < min_v.size(); i++){
        cout << i << " " << min_v[i] << " " << max_v[i] << '\n';
    }
    cout << cnt <<'\n';
    return ok;
}





/*
#include <iostream>

#include <vector>
using namespace std;
#define MAX_N 200001
#define rint register int

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
    if(mFrom == 1){
        
        v.erase(v.begin() + mFrom - 1, v.begin() + mTo);
        min_v.erase(min_v.begin() + mFrom - 1, min_v.begin() + mTo);
        max_v.erase(max_v.begin() + mFrom - 1, max_v.begin() + mTo);
    }
    else if(mTo == cnt){
        minV = v[mFrom - 2];
        maxV = v[mFrom - 2];

        v.erase(v.begin() + mFrom - 1, v.begin() + mTo);
        min_v.erase(min_v.begin() + mFrom - 1, min_v.begin() + mTo);
        max_v.erase(max_v.begin() + mFrom - 1, max_v.begin() + mTo);

        for(rint i = mFrom - 2; i >= 0; i--){
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
    }
    else{
        minV = min_v[mTo];
        maxV = max_v[mTo];

        v.erase(v.begin() + mFrom - 1, v.begin() + mTo);
        min_v.erase(min_v.begin() + mFrom - 1, min_v.begin() + mTo);
        max_v.erase(max_v.begin() + mFrom - 1, max_v.begin() + mTo);

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
    cout << "\n\n";
    cout << cnt << "\n";
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << ' ';
    }
    cout << "\n";
    for(int i = 0; i < min_v.size(); i++){
        cout << i << " " << min_v[i] << " " << max_v[i] << '\n';
    }
    cout << cnt <<'\n';
    return ok;
}
*/



/*
#define MAX_N 200001
#define rint register int
int renewed, length;
int arr[MAX_N];
int maxx[MAX_N];
int minn[MAX_N];
 
void init(int N, int mValue[])
{
    length = N;
    for (rint i = 0; i < N; i++) {
        arr[i] = minn[i] = maxx[i] = mValue[i];
    }
     
    for (rint i = length - 2;i >= 0;i--) {
        if (maxx[i] < maxx[i + 1]) maxx[i] = maxx[i + 1];
        if (minn[i] > minn[i + 1]) minn[i] = minn[i + 1];
    }
}
void add(int M, int mValue[])
{
    for (rint i = 0; i < M; i++) {
        arr[length + i] = minn[length + i] = maxx[length + i] = mValue[i];
    }
    length += M;
 
    for (rint i = length - 2;i >= 0;i--) {
        if (maxx[i] >= maxx[i + 1] && i < length - M) break;
        if (maxx[i] < maxx[i + 1]) maxx[i] = maxx[i + 1];
    }
     
    for (rint i = length - 2;i >= 0;i--) {
        if (minn[i] <= minn[i + 1] && i < length - M) break;
        if (minn[i] > minn[i + 1]) minn[i] = minn[i + 1];
    }
}
void erase(int mFrom, int mTo)
{
    int gap = mTo - mFrom + 1;
     
    if (mTo == length) {
        length -= gap;
        minn[length - 1] = maxx[length - 1] = arr[length - 1];
 
        for (rint i = length - 2;i >= 0;i--) {
            maxx[i] = (arr[i] > maxx[i + 1]) ? arr[i] : maxx[i + 1];
            minn[i] = (arr[i] < minn[i + 1]) ? arr[i] : minn[i + 1];
        }
    }
     
    else {
        mFrom--;
        for (rint i = mFrom; i + gap < length; i++) {
            arr[i] = arr[i + gap];
            maxx[i] = maxx[i + gap];
            minn[i] = minn[i + gap];
        }
        length -= gap;
 
 
        for (rint i = mFrom - 1; i >= 0; i--) {
            maxx[i] = (arr[i] > maxx[i + 1]) ? arr[i] : maxx[i + 1];
            minn[i] = (arr[i] < minn[i + 1]) ? arr[i] : minn[i + 1];
        }
    }
}
int find(int K)
{
    return maxx[length - K] - minn[length - K];
}
*/

