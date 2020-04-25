class Solution {
public:
    bool canJump(vector<int>& nums) {
        
        /*
        // O(N log N) solution
        set<int> pos;
        pos.insert(0);
        int sz = nums.size();
        for(int i = 0; i < sz - 1 && !pos.empty(); ++i){
            pos.insert(i + nums[i]);
            while(!pos.empty() && (*pos.begin()) == i)
                pos.erase(pos.begin());
        }
        return !pos.empty();
        */
        
        // O(N) solution
        
        int max_possible = 0;
        int sz = nums.size();
        
        for(int i = 0; i < sz && max_possible >= i; ++i){
            max_possible = max(max_possible, i + nums[i]);
            if(max_possible >= sz - 1)
                return true;
        }
        return false;
        
    }
};
