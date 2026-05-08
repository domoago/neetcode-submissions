class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        if (s.size() != t.size())
        {
            return false;
        }
        int alpha[26] = {0};
        for (int i = 0; i < s.size(); i++)
        {
            alpha[s[i] - 'a']++;
            alpha[t[i] - 'a']--;
        }
        for (const auto& x : alpha)
        {
            if (x)
            {
                return false;
            }
        }
        return true;
    }
};
