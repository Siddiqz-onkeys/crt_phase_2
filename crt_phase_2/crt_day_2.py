#print("CRT DAY 2")
'''#SELECTION SORT

def selectionSort(array, size):
	
	for ind in range(size):
		min_index = ind
		for j in range(ind + 1, size):
			# select the minimum element in every iteration
			if array[j] < array[min_index]:
				min_index = j
		# swapping the elements to sort the array
		(array[ind], array[min_index]) = (array[min_index], array[ind])

arr = [159,257963,22256,1,25,316]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
'''


#insertion sort
'''
def ins_sort(l):
    siz=len(l)
    for i in range(siz):
        key=l[i]
        j=i-1
        while j>=0 and l[j]>key:
            l[j+1]=l[j]
            j-=1
        l[j+1]=key
    print("The sorted array is: ",l)
print("day")
l=[25,1,635,25947,1256384,0,1547]
print(l)
ins_sort(l) '''

'''
#Merge sort
def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        #left array
        L=arr[:mid]

        #right array
        R=arr[mid:]
        #recursivvely call ing the ufnction
        mergesort(L)
        mergesort(R)

        i=0
        j=0
        k=0

        #comparing left and right
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        
        #to add the remaining elemetns if any
            #on lef tside
        if i <len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        
        #on irght side
        if j<len(R):
            arr[k]=L[j]
            j+=1
            k+=1

arr=[10,0,25,15,16]
print("Befor: ",arr)
mergesort(arr)
print("After: ",arr)   '''
'''   
#Quick sort
def quick_sort(arr):
    n=len(arr)
    pivot=arr[n-1]
    j=0
    i=j-1
    while j in range(0,n):
        if arr[j]<pivot:
            i+=1
            arr[i]=arr[j]
    arr[i+1]=pivot
    L=arr[:i+1]
    R=arr[i+2:]
    quick_sort(L)
    quick_sort(R)

arr=[15,1,69,35,56]
print(arr)
quick_sort(arr)
print(arr) '''

'''
#quick sort
def partition(arr,low,high):
    print("problme")
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            print("hh")
            i+=1
            (arr[i],arr[j])=(arr[j],arr[i])
    (arr[i+1],arr[high])=(arr[high],arr[i+1])
    return i+1
def quick_sort(arr,low,high):
    if low<high:
        pivot=partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot-1,high)



arr=[15,1,69,35,56]
quick_sort(arr,0,len(arr)-1) '''



