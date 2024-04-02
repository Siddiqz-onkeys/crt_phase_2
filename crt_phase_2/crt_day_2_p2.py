print("Linked lists...")

#################TO CREATE A  NEW NODE #####################
class Node:
    def __init__(self,data) :
        self.data=data
        self.next=None


        
###################TO ADD AN ELEMENT AT THE BEGGINING OF THE LIST##############
def insert_at_begg(head,data):
    New_node=Node(data)
    New_node.next=head
    head=New_node
    return head



###############TO ADD AN ELEMENT AT THE END OF THE LIST #################
def insert_at_end(head,data):
    new_node=Node(data)
    temp=head
    while temp.next!=None:
        temp=temp.next
    temp.next=new_node


    
###############TO FIND THE COUNT OF THE LIST #################
def count_fun(head):
    count=0
    temp=head
    while temp!=None:
        count+=1
        temp=temp.next
    return count




#####################TO FIND THE MID VALUE OF THE LIST##################
def mid_val(head,count):
    temp=head
    count_2=0
    while temp!=None:
        count_2+=1
        if count_2==(count//2)+1:
            print("MID VALUE OF THE LIST IS: ",temp.data)
            break
        temp=temp.next


        
###################TO DELETE A DATA FROM THE LINKED LIST##################
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


        

#######################TO DELETE THE MID VALUE ######################
def remove_mid(head,total):
    cou=0
    temp=head
    while temp!=0:
        cou+=1
        if cou==total//2:
            print("Deleting the mid value:",temp.data)
            temp.data=None
            temp_prev.next=temp.next
            temp.next=None
            break
        temp_prev=temp
        temp=temp.next


        

##################TO DISPLAY THE ENTIRE LINKED LIST##################        
def display(head):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next


        


######################################START OF THE MAIN BODY###################################
head=Node(3)
second=Node(23)
third=Node(43)
head.next=second #linkning one and two
second.next=third #linking two and three
print("LIST BEOFRE:")
display(head)
print()

#####################inserting a new element###################
head=insert_at_begg(head,63) #AT THE BEGINNING
insert_at_end(head,61)#AT THE ENDING
##########LIST AFTER INSERTING AT THE BEGINNING AND AT THE END
print("LIST AFTER INSERTING AT THE BEGINNING AND AT THE END:")
display(head)
print()

##########PRINTING THE COUNT OF THE LINKED LIST
total=count_fun(head)
print("COUNT OF THE LINKED LIST: ",total)
print()

#############TO GET THE MID VALUE
mid_val(head,total)
print()
################TO DELETE A LINK
remove_link(head,23)
print("THE LIST AFTER THE FIRST REMOVAL:")
display(head)
print()

#REMOVINBG THE MID VALUE FORM THE LIST
print("AFTER THE REMOVAL OF THE MID VALUE:")
remove_mid(head,total)
display(head) 

#display(head)
#print("After")
#display(head)





    

#create a funciton to delete the value given by the user
