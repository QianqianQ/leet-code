#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;

class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		unordered_map<int, int> lookup;
		for (int i = 0; i<nums.size(); i++)
		{
			if (lookup.count(target - nums[i]))
				return { lookup[target - nums[i]],i };
			lookup.insert({ nums[i],i });
		}
		return {};
	}
};

int main(void)
{
	Solution s;
	vector<int> nums = { 2,7,11,15 };
	int target = 9;
	vector<int> result = s.twoSum(nums, target);
	for (auto i = result.begin();i!=result.end();i++)
	{
		cout<<*i<<endl;
	}
}
