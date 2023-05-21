/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        stack<int> st;
        ListNode * p=head;
        while(p!=nullptr)
        {
            st.push(p->val);
            p=p->next;
        }

        p=head;
        while(!st.empty())
        {
            int x=st.top();
            if(x!=p->val)
                return false;
            st.pop();
            p=p->next;
        }
        return true;

    }
};