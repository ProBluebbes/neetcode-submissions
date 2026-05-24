class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();

        int start = 0;
        int end = 0;
        int sum = nums[0];
        int cumulativeSum = nums[0];

        for (int i = 1; i < n; i++) {
            cumulativeSum += nums[i];

            // CHECK IF RESETING
            if (nums[i] > cumulativeSum) {
                start = i;
                end = i;
                cumulativeSum = nums[i];
                if (cumulativeSum > sum)
                    sum = cumulativeSum;
            }
            // CHECK IF ADDING IS WORTHWHILE
            else if (cumulativeSum >= sum) {
                end = i;
                sum = cumulativeSum;
            }
        }

        return sum;
    }
};
