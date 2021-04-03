'''
A permutation of integers 1,2,…,n is called beautiful if there are no adjacent elements whose difference is 1.

Given n, construct a beautiful permutation if such a permutation exists.

Input

The only input line contains an integer n.

Output

Print a beautiful permutation of integers 1,2,…,n. If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".

Constraints

    1≤n≤106


Example 1

Input:
5

Output:
4 2 5 3 1

Example 2

Input:
3

Output:
NO SOLUTION'''

def beatiful_shuffle(ls):
    #rearrange list so all second elements are in a row 
    # e.g [1,2,3,4]--> [2,4,1,3]
    new =  []
    n = 1 
    while(n<len(ls)):
        new.append(ls[n])
        n+=2
    n=0
    while(n<=len(ls)-1):
        new.append(ls[n])
        n+=2
    
    return new

seed = int(input())

#edge cases 
if seed == 2 or seed == 3:
    print("NO SOLUTION")

elif seed == 1:
    print(1)

else:
    ls = [x for x in range(1,seed+1)]
    solution = None
    print(*beatiful_shuffle(ls), sep=" ")
