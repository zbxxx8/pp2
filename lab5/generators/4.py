def squares(nums):
    for i in nums:
        yield (i*i)
nums=[10,11,12,13,14,15]
square_nums =  squares(nums)
for num in square_nums:
    print (num) 