tuple1 = tuple([1, 2, 3, 4, [5, 6, 7, 8]])
print(tuple1)
for i in range(len(tuple1)):
    if type(tuple1[i]) == list:
        print(tuple1[i])