n=3
size=(2*n)-1
for i in range(size):
    stars=""
    for j in range(size):
        min_val=min(i,j)
        max_val=max(i,j)
        f1=n-min_val
        f2=n+max_val-(size-1)
        pick_val=max(f1,f2)
        stars=stars+" "+str(pick_val)
    print(stars)
     