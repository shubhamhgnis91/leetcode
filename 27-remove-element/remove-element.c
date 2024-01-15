int removeElement(int* nums, int numsSize, int val){
    int k=0;
    int temp[100];

    for(int i=0,j=0;i<numsSize;i++)
    {
        if(nums[i]!=val)
        {
            temp[j++]=nums[i];
            k++;
        }
    }
    for(int i=0;i<k;i++)
        nums[i]=temp[i];

    return k;
}