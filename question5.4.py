def outer_fun(a,b):
    def addition(a,b):
        return a + b
    add = addition(a,b)
    return add + 10
result = outer_fun(5,10)
print(result)
