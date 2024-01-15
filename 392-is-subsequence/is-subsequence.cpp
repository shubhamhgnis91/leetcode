class Solution {
    public:
    bool isSubsequence(string s, string t) 
    {
        const char *ptr = t.c_str();
        int start = 0;
        for(int i=0; i<s.size(); i++)
        {
            const char *p = strchr(ptr + start, s[i]);
            if (p == NULL)
                return false;
            start = p - ptr + 1;
        }
        return true;
    }
};