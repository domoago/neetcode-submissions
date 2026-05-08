class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> output;
        unordered_map<int, int> mp;
        vector<vector<int>> bucket;
        bucket.resize(nums.size() + 1);
        for (int i = 0; i < nums.size(); i++)
        {
            if (mp.count(nums[i]) == 0)
            {
                mp.insert({nums[i], 1});
            }
            else
            {
                mp[nums[i]]++;
            }
        }
        for (auto& x : mp)
        {
            bucket[x.second].push_back(x.first);
        }
        for (int i = bucket.size() - 1; i >= 0 && k > 0; i--)
        {
            if (bucket[i].empty() == false)
            {
                for (int j = 0; j < bucket[i].size(); j++)
                {
                    output.push_back(bucket[i][j]);
                    k--;
                }
            }
        }
        return output;
    }
};
