class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs)
    {
        vector<vector<string>> output;
        unordered_map<string, vector<string>> mp;
        for (int i = 0; i < strs.size(); i++)
        {
            string copy = strs[i];
            sort(copy.begin(), copy.end());
            mp[copy].push_back(strs[i]);
        }
        for (auto i = mp.begin(); i != mp.end(); i++)
        {
            output.push_back(i->second);
        }
        return output;
    }
};
