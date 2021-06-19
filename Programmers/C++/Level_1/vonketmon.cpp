#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> nums)
{
    int answer;
    vector<int> v = {};
    int num = nums.size()/2;
    for(int i =0;i<nums.size();i++){
        if(find(v.begin(),v.end(),nums[i])==v.end())
            v.push_back(nums[i]);  
    }
    if(num>v.size())
        answer=v.size();
    else
        answer=num;
    return answer;
}