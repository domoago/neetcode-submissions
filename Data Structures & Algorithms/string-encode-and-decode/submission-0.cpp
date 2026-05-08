class Solution {
public:

    string encode(vector<string>& strs)
    {
        string output{};
        for (auto& str : strs)
        {
            output = output + str + ";";
        }
        return output;
    }

    vector<string> decode(string s)
    {
        string str{};
        vector<string> output;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] != ';')
            {
                str = str + s[i];
            }
            else
            {
                output.push_back(str);
                str = "";
            }
        }
        return output;
    }
};
