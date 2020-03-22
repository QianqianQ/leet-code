#include <iostream>
#include <math.h> 

class Solution {
public:
    int reverse(int x) {
        int INT_MAX = pow(2,31) - 1;
        int INT_MIN = -pow(2,31);
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > INT_MAX/10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
            if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
};

int main(void)
{
	Solution s;
	int res = s.reverse(-123);
    std::cout<<res<<std::endl;
}