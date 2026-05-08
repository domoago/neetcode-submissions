class Solution
{
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs)
    {
        unordered_map<string, vector<string>> mp;
        vector<vector<string>> output;
        for (int i = 0; i < strs.size(); i++)
        {
            string str2 = strs[i];
            sort(str2.begin(), str2.end());
            if (mp.count(str2))
            {
                mp.at(str2).push_back(strs[i]);
            }
            else
            {
                mp.insert({str2, {strs[i]}});
            }
        }
        
        for (const auto& x : mp)
        {
            output.push_back(x.second);
        }
        return output;
    }
};
