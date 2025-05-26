def each_cons(lst, n):
    return [lst[i:i+n] for i in range(len(lst) - n + 1)]
print(each_cons([1, 2, 3, 4], 2))  

print(each_cons([1, 2, 3, 4], 3))  

