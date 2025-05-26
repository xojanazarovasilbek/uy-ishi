def distinct(arr):
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(distinct([1, 1, 2]))           
print(distinct([1, 2, 1, 1, 3, 2])) 
