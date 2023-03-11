def gen(n):
    for i in range(1,int(n**0.5)+1):
        yield(i*i)
squares =gen(25)
for a in squares:
    print(a)