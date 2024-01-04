class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        for(int i = 0; i < flowerbed.size() && n > 0 ; i++)
        {
            if( flowerbed[i] == 1 )
            {
                i++;
                continue;
            }

            bool left_empty = ( i==0 || flowerbed[i-1]==0);
            bool right_empty = (i==flowerbed.size() - 1 || flowerbed[i+1]==0);

            if(left_empty && right_empty)
            {
                n--;
                flowerbed[i++]=1;
            } 
        }

        return n==0;
    }
};