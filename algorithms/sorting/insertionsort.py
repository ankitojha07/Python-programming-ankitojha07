def insertSort(a):
    n = len(a)
    for i in range(1,n):
        
        cvalue = a[i]
        pos = i
        while pos>0 and a[pos-1]>cvalue:
            a[pos]=a[pos-1]
            pos=pos-1
        a[pos] = cvalue

a = [2,5,1,8,6,9,12,11,18,16]
print('Before sorting : ',a)

insertSort(a)
print('After sorting : ',a)