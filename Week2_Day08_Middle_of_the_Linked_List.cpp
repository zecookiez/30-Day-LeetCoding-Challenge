/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        
        ListNode* pFast = head;
        ListNode* pSlow = head;
        
        /*
        
            O(1) memory approach -> Have a pointer that moves twice as fast as the other one.
                                    The distance covered will be half once the fast one has reached the end.
        
        */
        
        while(pFast && pFast->next){
            pSlow = pSlow->next;
            pFast = pFast->next->next;
        }
        
        return pSlow;
        
    }
};
