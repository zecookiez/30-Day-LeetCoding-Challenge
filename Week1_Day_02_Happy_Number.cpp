class Solution {
public:
    
    bool isHappy(int n) {
        return floyd_cycle(n) == 1;
    }
    
    int f(int num){ // Generate succesor of num
        int sum = 0;
        while(num > 0){
            sum += (num % 10) * (num % 10);
            num /= 10;
        }
        return sum;
    }
    
    /*
      We can use cycle detection to find when we start repeating
      As 1^2 = 1, we only need to look if the beginning of the cycle is equal to 1.
      
      An O(1) cycle detection algorithm is Floyd's Tortoise and Hare, where one pointer moves twice as fast as the other.
      https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare
    */
    
    int floyd_cycle(int start){
        int tort = f(start), hare = f(f(start));
        while(tort != hare){
            tort = f(tort);
            hare = f(f(hare));
        }
        return tort;
    }
    
};
