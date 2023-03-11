def gen(n):
    for i in range(n):
        if i%2==0:
            yield i 
n=int(input())
even_nums=gen(n)
for a in even_nums:
    print(a,end=",")