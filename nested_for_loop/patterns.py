# step1:enni rows enni cols vunnai
# step2:first row lo enni stars vunnai
# step3:stars incre/decre
# step4:first row lo enni spaces vunnai
# step5:spaces incre/decre 

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



for i in range(5):
    stars=""
    for j in range(5):
        if(i==0 or j==0 or i==4 or j==4):
            stars=stars+" *"
        else:
            stars=stars+"  "
    print(stars)


for i in range(5):
    stars=""
    for k in range(0+i):
        stars=stars+"  "
    for j in range(5-i):
        stars=stars+" *"
    print(stars)

for i in range(5):
    stars=""
    for k in range(4-i):
        stars=stars+"  "
    for j in range(1+i):
        stars=stars+" *"
    print(stars)



n=8

for i in range(n):
    stars=""
    for k in range(n-1-i):
        stars=stars+" "
    for j in range(1+i):
        stars=stars+" *"
    print(stars)

for i in range(n):
    stars=""
    for k in range(0+i):
        stars=stars+" "
    for j in range(n-i):
        stars=stars+" *"
    print(stars)
























for i in range(5):
    stars=""
    for j in range(5-i):
        stars=stars+" *"
    print(stars)










for i in range(5):
    stars=""
    for j in range(1+i):
        stars=stars+" *"
    print(stars)
    

