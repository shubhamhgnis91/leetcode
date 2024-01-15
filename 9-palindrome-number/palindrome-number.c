#include <string.h>

bool isPalindrome(int x){

    if(x<0 || (x!=0 && x%10==0))
        return false;

    char s[11];
    sprintf(s,"%d",x);
    for(int i=0;i<strlen(s)/2;i++)
        if(s[i]!=s[strlen(s)-i-1])
            return false;
    return true;
    
}