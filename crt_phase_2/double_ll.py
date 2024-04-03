class Node:
    def __init__(self,data) :
        self.prev=None
        self.data=data
        self.next=None

def insert_at_end(head,data):
    temp=head
    new_node=Node(data)
    while temp.next!=None:
        temp=temp.next
    temp.next=new_node
    new_node.prev=temp
        
def insert_at_beg(head,data):
    new_node=Node(data)
    new_node.next=head
    head=new_node
    return head

def remove_link(head,data):
    temp=head
    while temp!=None:
        if temp.next.data==data:
            temp.next=temp.next.next
            temp.next.prev=temp
        temp=temp.next
        """if temp.data==data:
            prev_link=temp.prev
            next_link=temp.next
            temp.prev=None
            temp.next=None
            temp.data=None
            if next_link!=None:
                next_link.prev=prev_link
            prev_link.next=next_link
        prevs=temp
        temp=temp.next"""   

            
def display(head):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next
##############START OF THE MAIN PROGRAM##################
head=Node(3)
insert_at_end(head,5)
#print(head.next.data)
insert_at_end(head,78)
head=insert_at_beg(head,66)
head=insert_at_beg(head,81)
print("Before deletion:")
display(head)
print("After deletion:")
remove_link(head,3)
display(head)















#skip and delete arethe first two number 
#so skip for n links and delete m links and repeat that for the entire linked list0