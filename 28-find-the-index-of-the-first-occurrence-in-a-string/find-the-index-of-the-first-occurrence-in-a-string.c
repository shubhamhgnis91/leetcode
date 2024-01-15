#include <string.h>

int strStr(char * haystack, char * needle){
    char *res=strstr(haystack,needle);
        if(res)
            return res-haystack;
        return -1;
}