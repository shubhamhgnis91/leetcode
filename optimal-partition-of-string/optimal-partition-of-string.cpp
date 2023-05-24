class Solution {
public:
    int partitionString(string s) {
        unordered_set<char> st;
        int count=0;
        for(int i=0;i<s.size();i++)
        {
            if(st.find(s[i])!=st.end())
            {
                st.clear();
                st.insert(s[i]);
                count++;
            }
            else
                st.insert(s[i]);
        }
        return count+1;
    }
};