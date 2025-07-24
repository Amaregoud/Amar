def findpairs(arr):
    s=set()
    for (x,y) in arr:
        s.add((x,y))
        if (y,x) in s:
            print((x,y))
arr=[(2,3),(4,5),(6,7),(9,0),(0,9)]
findpairs(arr)