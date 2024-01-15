int jump(int* nums, int numsSize)
{
    int left=0,right=0,jumps=0;
    while(right<numsSize-1)
    {
        int maxr=0;
        for(int i=left;i<right+1;i++)
            maxr=mx(maxr,i+nums[i]);
        left=right+1;
        right=maxr;
        jumps++;
    }
    return jumps;
}

int mx(int x, int y)
{
    if(x<y)
        return y;
    return x;
}