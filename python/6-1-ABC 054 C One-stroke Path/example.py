import itertools

#permutation
for i in itertools.permutations([0,1,2], 3):
    print(i)


for i in itertools.combinations([0,1,2,3], 2):
    print(i)