/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* middleNode(struct ListNode* head){
    struct ListNode *p=head;
    for(struct ListNode *q=head; q!=NULL && q->next!=NULL; p=p->next, q=q->next->next)
        ;
    return p;
}