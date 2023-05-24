
int leftSum(int* nums, int numsSize, int k)
{
    if(k==0)
        return 0;
    int sum=0;
    for(int i=k-1;i>=0;i--)
        sum+=nums[i];
    return sum;
}

int rightSum(int* nums, int numsSize, int k)
{
    if(k==numsSize)
        return 0;
    int sum=0;
    for(int i=k+1;i<numsSize;i++)
        sum+=nums[i];
    return sum;
}

int pivotIndex(int* nums, int numsSize){
    int flag=0,pivot;
    for(int i=0;i<numsSize;i++)
        if(leftSum(nums,numsSize,i)==rightSum(nums,numsSize,i))
        {
            flag=1;
            pivot=i;
            break;
        }
    if(flag==0)
        return -1;
    
    return pivot;
    
}