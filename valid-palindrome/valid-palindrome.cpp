#include<cctype>
class Solution {
public:
    bool isPalindrome(string s) {
        int l=0,h=s.size()-1;

        while(l<=h)
        {
            
            if(!isalnum(s[l]))
            {
                l++;
                continue;
            }
            else if(!isalnum(s[h]))
            {
                h--;
                continue;
            }
            else
                if(tolower(s[l])!=tolower(s[h]))
                    return false;
            l++;
            h--;
        }
        return true;
    }
};