arr=[50,3,10,7,40,80]
d={}
for i in range(len(arr)):
    l=[]
    start=arr[i]
    l.append(start)
    length=1
    for j in range(i+1,len(arr)):
        if all(arr[j] > x for x in l):
            length+=1
            l.append(arr[j])
    d[length]=l

print("longest length",max(d.keys()),"longest increasing subsequence:",d[max(d.keys())])

print(d)

