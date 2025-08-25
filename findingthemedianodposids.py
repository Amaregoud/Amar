n=int(input())
arr=list(map(int,input().split()))
pos_ids=[x for x in arr if x > 0]
if len(pos_ids)==0:
    print(-1)
else:
    middle_index=len(pos_ids)//2
    print(pos_ids[middle_index])
    