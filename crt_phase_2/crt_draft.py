L=[1,3,6,7,9,5,2]
strt=0
end=len(L)-1
mid=(strt+end)//2
flag=0
while strt<=end:
    if L[mid-1]<L[mid] and L[mid+1]<L[mid]:
        flag=1
        print("Peak found at the index:",mid)
        print("The peak flow is:",L[mid-1],L[mid],L[mid+1])
        break
    else:
        strt=mid
        print("11")
if flag!=1:
    while strt<=end:
        if L[mid-1]<L[mid] and L[mid+1]<L[mid]:
            print("Peak found at the index:",mid)
            print("The peak flow is:",L[mid-1],L[mid],L[mid+1])
        else:
            end=mid
