def revese_count(n):
    for i in range(n,0,-1):
        yield i
    else:
        yield 0
for a in revese_count(25):
    print(a,end=" ")