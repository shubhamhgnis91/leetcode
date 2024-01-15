class Solution {
public:
    bool isPowerOfTwo(int n) {
        double x=log(n)/log(2);
        return (n>0 && (x-(int)x)<0.000000001 ) ? true:false;
    }
};