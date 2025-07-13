
def pairTargetSum(arr, target):
    pass
    set1= set()
    pair=[]
    for i in arr:
        diff = target-i
        if diff in set1:
            pair.append((i,diff))
        set1.add(i)

    return  pair







a=pairTargetSum([1,4,2,5,-2], 3)
print(a)
