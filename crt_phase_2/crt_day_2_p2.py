print("Linked lists...")
class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None
def insert_at_begg(head,data):
    New_node=Node(data)
    New_node.next=head
    head=New_node
    return head

def insert_at_end(head,data):
    new_node=Node(data)
    temp=head
    while temp.next!=None:
        temp=temp.next
    temp.next=new_node

def count_fun(head):
    count=0
    temp=head
    while temp!=None:
        count+=1
        temp=temp.next
    return count

def mid_val(head,count):
    temp=head
    count_2=0
    while temp!=None:
        count_2+=1
        if count_2==(count//2)+1:
            print("Mid value is: ",temp.data)
            break
        temp=temp.next  

def remove_link(head,data):
    temp=head
    while temp!=None:
        if temp.data==data:
            temp.data=None
            temp_prev.next=temp.next
            temp.next=None
            break
        temp_prev=temp
        temp=temp.next
        
def display(head):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next

head=Node(3)
second=Node(23)
third=Node(43)
head.next=second #linkning one and two
second.next=third #linking two and three
head=insert_at_begg(head,63)
insert_at_end(head,61)
display(head)  
total=count_fun(head)
print("Count for the linked list is: ",total)
mid_val(head,total)
remove_link(head,23)
display(head) 

#display(head)
#print("After")
#display(head)





    

#create a funciton to delete the value given by the user