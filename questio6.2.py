tuples = (('a',44),('b',25),('c',9),('d',52))
tuples = tuple(sorted(list(tuples), key=lambda x: x[1]))
print(tuples)

