nums = [1,2,3,4,5,6,7,8,9]
my_list = [n for n in nums]
print(my_list)

print([n*n for n in nums])
print(list(map(lambda n: n*n, nums)))

my_list = [(letter, num, a) for letter in 'abcd' for num in range(4) for a in range(5)]
print(my_list)

names = ['ram', 'shyam', 'mohan','hari']
ages =['129', '123', '134', '126']
print({name:age for name, age in zip(names, ages)})

a = [2,4,5,3,2,4,2,4,2,4,43,4,4,2,4,5,4]

print({n for n in a})

