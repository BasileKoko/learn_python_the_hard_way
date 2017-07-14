def square_number(nums):
    for i in nums:
        yield i*i

my_nums = square_number([1,2,3,4,5])
print(my_nums)
print(next(my_nums))

# Generators with list comprehension

my_nums2 = (x*x for x in [4,6,3,7,2])
print(my_nums2)
print(next(my_nums2))
