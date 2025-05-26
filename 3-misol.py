def add_length(s):
    return [f"{soz} {len(soz)}" for soz in s.split()]

print(add_length("apple ban"))        
print(add_length("you will win"))     
