def recurSum(i):
    if i<= 1:
        return i
    return i + recurSum(i - 1)
i = 10
print(recurSum(i))

