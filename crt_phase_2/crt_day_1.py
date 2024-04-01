'''
#LINEAR SEARCH
L=[12,25,66,258,963]
te=int(input("enter the target element:"))
for i in range(0,len(L)):
    if te==L[i]:
        print("Element is found at:",i+1)
        break;'''


'''
#BINARY SEARCH WITH RECURSSIVE FUNCTION#
def binary_Search(strt,end,L,tr_el):
    mid=(strt+end)//2
    if tr_el==L[mid]:
        print("Element found at the index:",mid)
    elif tr_el>L[mid]:
        strt=end+1
        binary_Search(strt,end,L,tr_el)
    elif tr_el<L[mid]:
        end=strt+1
        binary_Search(strt,end,L,tr_el)

L=[12,15,26,38,59]
strt=0
end=len(L)
tr_el=12
binary_Search(strt,end,L,tr_el) '''
    



'''
#BINARY SEARCH WIHOUT FUNCITONS
L=[12,15,26,38,59]
strt=0
end=len(L)
#mid=(strt+end)//2
mid=strt+(end-strt)//2 #this is to satisfy hidden test cases that press in the integer limit 
tr_el=15
while strt<=end:
    if tr_el==L[mid]:
        print("Element found at the index:",mid)
        break;
    elif tr_el<L[mid]:
        end=mid-1
    elif tr_el>mid+1:
        strt=mid+1
    mid=(strt+end)//2 '''
'''
#first and last occurances of a number in the list using binary search
def first_occ(strt,end,T):
   #for the first occurance
   while strt<=end:
      mid=(strt+end)//2
      if L[mid]==T:
         first_occr=mid
         end=mid-1
      elif L[mid]<T:
         strt=mid+1
      elif L[mid]>T:
         end=mid-1
   return first_occr

def last_occ(strt,end,T):
   #for the first occurance
   while strt<=end:
      mid=(strt+end)//2 
      if L[mid]==T:
         last_occr=mid
         strt=mid+1
      elif L[mid]<T:
         strt=mid+1
      elif L[mid]>T:
         end=mid-1
   return last_occr

L=[1,4,4,4,9,13,15,15]
strt=0
end=len(L)-1
mid=(strt+end)//2
print("The first and last occurances of the number 4 are: ",first_occ(strt,end,4),"and ",last_occ(strt,end,4))
print("The first and last occurances of the number 15 are: ",first_occ(strt,end,15),"and ",last_occ(strt,end,15)) '''


'''
#finding the peak point of the given list
L=[1,3,6,7,9,5,2]
strt=0
end=len(L)-1
flag=0
while strt<=end:
    mid=(strt+end)//2
    if L[mid-1]<L[mid] and L[mid+1]<L[mid]:
        flag=1
        print("Peak found at the index:",mid)
        print("The peak flow is:",L[mid-1],L[mid],L[mid+1])
        break
    elif L[mid]>L[mid-1]:
        strt=mid
    elif L[mid+1]>L[mid]:
        end=mid '''

# BOOK ALLOCATION PROBLEM
def ispossible(stu,pages,mid):
    sum1=0
    nos=1 #no of stubents
    for i in range(0,len(pages)):
        if sum1+pages[i]<=mid:
            sum1+=pages[i]
        else:
            nos+=1 #passign to the next student
            if nos>stu or pages[i]>mid: #not possible case
                return False
            sum1=pages[i]  # asssigs to the next element
    return True

def bin(stu,pages):
    sum_of_p=0
    for i in pages:
        sum_of_p+=i
    s=0
    e=sum_of_p
    mid=s+(e-s)//2  #max no of pages which the student could be allocated 
    while s<=e:
        if ispossible(stu,pages,mid):
            ans=mid
            e=mid-1
        else:
            s=mid+1
        mid=s+(e-s)//2
    return ans

pages=[10,20,30,40]
print("Enter the number of students:")
stu=int(input())
print(bin(stu,pages))




