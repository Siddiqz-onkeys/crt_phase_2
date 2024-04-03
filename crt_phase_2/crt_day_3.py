'''class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None

def display(head):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next

def display_rev(head):
    curr=head
    prev=None
    while(curr!=None):
        next_el=curr.next
        curr.next=prev
        prev=curr
        curr=next_el
    head=prev
    return head

def rev_nmbrd(head,n):
    curr=head
    prev=None
    count=0
    while curr!=None and count<n:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
        count+=1
    if next!=None:
        head.next=rev_nmbrd(next,n) 
    head=prev
    return head

head=Node(3)
second=Node(23)
third=Node(43)
fourth=Node(63)
fifth=Node(61)
head.next=second #linkning one and two
second.next=third #linking two and three
third.next=fourth #linking third and fourth
fourth.next=fifth #linking fourth and fifth
display(head)
print("Printing the linked list in reverse order:")
rev_head=display_rev(head)
display(rev_head)
print("printing the list in partitioned revere order:")
display(rev_nmbrd(head,3))

'''



## arr=[2,1,2,2,0,1,2,0,0,1,1] output should be 00011112222
'''def bubble_sort(L):
    n=len(L)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if L[j]>L[j+1]:
                temp=L[j]
                L[j]=L[j+1]
                L[j+1]=temp'''
        
'''L=[2,1,2,2,0,1,2,0,0,1,1]
n=len(L)
cou_0=0
cou_1=0
cou_2=0
for i in L:
    
    if i==0:
        cou_0=cou_0+1
        
    elif i==1:
        cou_1=cou_1+1
    
    elif i==2:
        cou_2=cou_2+1
    #for 0s
index=0
while index<cou_0:
    L[index]=0
    index+=1
while index<cou_1:
    L[index]=1
    index+=1
while index<cou_2:
    L[index]=2
    index+=1
    

print(L)'''


        
    
'''print("Before operation:",L)
bubble_sort(L)
print("After sorting:",L)'''


class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None

def insert_at_end(head,data):
    new_node=Node(data)
    temp=head
    while temp.next!=None:
        temp=temp.next
    temp.next=new_node

def display(head):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next

head1=Node(11)
insert_at_end(head1,22)
insert_at_end(head1,33)
print("First list is: ")
display(head1)
head2=Node(11)
insert_at_end(head2,22)
insert_at_end(head2,33)
print("Second list is: ")
display(head2)

'''print("hellll")
c0=0
c1=0
c2=0
temp=head
while temp!=None:
    if temp.data==0:
        c0+=1
    elif temp.data==1:
        c1+=1
    else:
        c2+=1
    temp=temp.next

temp_n=head
while c0!=0:
    temp_n.data=0
    temp_n=temp_n.next
    c0-=1
while c1!=0:
    temp_n.data=1
    temp_n=temp_n.next
    c1-=1
while c2!=0:
    temp_n.data=2
    temp_n=temp_n.next
    c2-=1
print("At the end")
display(head)'''



