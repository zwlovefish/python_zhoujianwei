sequence=[7,6,9,10,3,14,43,2,12,100]
print("原始的列表是：",end='')
print(sequence)


def bubblesort(seq):
    for i in range(len(seq)-1,-1,-1):
        for j in range(0,i):
            if seq[j]>seq[j+1]:
                temp=seq[j]
                seq[j]=seq[j+1]
                seq[j+1]=temp

                
bubblesort(sequence)
print("排序后的列表是：",end='')
print(sequence)
