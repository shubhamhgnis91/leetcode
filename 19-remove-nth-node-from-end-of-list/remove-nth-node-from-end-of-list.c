/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode *p;
   
    int size=0,i;
    
    for(p=head;p!=NULL;p=p->next,size++)
        ;
    
    if(size==1)
        return NULL;
    
    if(size==n)
        return head->next;
    
    i=size-n-1;
    p=head;
    for(int j=0;j<i;j++)
        p=p->next;
    
    p->next=p->next->next;
    return head; 
        
    
}