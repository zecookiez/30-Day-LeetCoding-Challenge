class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
    
        // Simulate the process, use a heap/priority queue to make the steps run in O(log N) time.
        
        // Since we run O(N) steps in the simulation, this runs in O(N log N).
        
        priority_queue<int> sorted_stones;
        
        for(int st : stones)
            sorted_stones.push(st);
        
        // Simulate the process while there are more than 1 stone left
        
        while(sorted_stones.size() > 1){
            
            // Heaviest stone
            
            int stone_a = sorted_stones.top(); sorted_stones.pop();
            
            // Second heaviest stone
            
            int stone_b = sorted_stones.top(); sorted_stones.pop();
            
            sorted_stones.push(stone_a - stone_b);
            
        }
        
        return sorted_stones.top();
    
    }
};
