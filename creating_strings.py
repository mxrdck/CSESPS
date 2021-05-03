import itertools

s = str(input())


perms = set(itertools.permutations(s))
perms = sorted(perms)
print(len(perms))
for perm in perms:
    print(*perm,sep="")