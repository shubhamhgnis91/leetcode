void insert(struct ListNode **head, int x)
{
    struct ListNode *p=(struct ListNode *)malloc(sizeof(struct ListNode));
    p->val=x;
    p->next=NULL;

    if(*head==NULL)
    {
        *head=p;
        return;
    }
    struct ListNode *q;
    for(q=*head;q->next!=NULL;q=q->next)
        ;
    q->next=p;    
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){

    if(l1==NULL&&l2==NULL)
        return NULL;
    
    if(l1==NULL)
        return l2;
    
    if(l2==NULL)
        return l1;

    struct ListNode *res=NULL,*p=l1,*q=l2;
    int carry=0;

    while(p!=NULL || q!=NULL)
    {
        int n1=p!=NULL ? p->val : 0;
        int n2=q!=NULL ? q->val : 0;
        int sum=n1+n2+carry;
        carry=sum/10;
        int last_digit=sum%10;
        insert(&res,last_digit);
        p=p!=NULL ? p->next : NULL;
        q=q!=NULL ? q->next : NULL;
    }

    if(carry)
        insert(&res,carry);

    return res;
}