
def selectSort(a):
    n = len(a)
    for i in range(n-1):
        pos = i
        for j in range(i+1,n):
            if a[j]<a[pos]:
                pos = j
        temp = a[i]
        a[i] = a[pos]
        a[pos] = temp

a = [7,9,3,5,1,92,5]
print('Original array : ',a)

selectSort(a)
print('After selection sort : ',a)
