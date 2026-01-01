#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>


using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        // pairmap for the correct order
        vector<pair<int, int>> v;
        for (int i = 0; i < nums.size(); i++) {
            v.push_back({nums[i], i});
        }

        // pre-sort array
        sort(v.begin(), v.end());

        // init values
        int left = 0;
        int right = v.size() - 1;

        // two pointers
        while (left < right) {
            int curr = v[left].first + v[right].first;
            if (curr < target) left++ ;
            else if (curr > target) right-- ;
            else {
                vector<int> res = {v[left].second, v[right].second};
                sort(res.begin(), res.end());
                return res;
            }
        }

        // base return
        return {};
    }
};
