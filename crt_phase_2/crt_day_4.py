###### Day 4 [IMple,emting the stacks]

def push(s,data):
    s.append(data)

def top(s):
    return s[-1]

def display(s):
    print("uuu")
    while len(s)!=0:
        print(s.pop())

def lis_stck(lis):
    stcked=[]
    for i in range(0,len(lis)):
        push(stcked,lis[i])
    return stcked

def nex_big(s):
    stck2=[]
    prev_top=top(s)
    while len(s)!=0:
        curr_top=top(s)
        if curr_top>prev_top:
            push(stck2,curr_top)
        else:
            push(stck2,-1)
        prev_top=curr_top
        s.pop
    return stck2
    
lis=[2,14,16,1,4,12]
stck=lis_stck(lis)
#print(top(stck))
#display(stck)
new_stck=nex_big(stck)
display(new_stck)
"""       
def rev_stk(s,s1):
    while len(s)!=0:
        push(s1,s.pop())       

s=[]
s1=[]
push(s,25)
push(s,66)
push(s,10)
push(s,59)
push(s,48)
rev_stk(s,s1)
display(s1)"""
"""s="[({)})]"
stck=[]
#def valid(s):
for i in range(0,len(s)):
    if s[i] in "{[(":
        push(stck,s[i])
    elif (s[i]=="}" and top(stck)=="{") or (s[i]=="]" and top(stck)=="[") or (s[i]==")" and top(stck)=="("):
        stck.pop()
    else:
        break
if len(stck)==0:
    print("valid")
else:
    print("Invalid")"""



#take list as input   [2,14,16,1,4,12]

#input ot the stack is 1 2 3 4 5
#output should be 1 2 3 4 5-+



