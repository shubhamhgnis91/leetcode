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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        unordered_map<ListNode*, int> um;

        for(auto it=headA; it!=NULL;it=it->next){
            um[it] = 1;
        }

        for(auto it=headB;it!=NULL;it=it->next){
            if(um.find(it)!=um.end()){
                return it;
            }
        }
        return NULL;

    }
};