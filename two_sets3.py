'''
Your task is to divide the numbers 1,2,…,n into two sets of equal sum.

Input

The only input line contains an integer n.

Output

Print "YES", if the division is possible, and "NO" otherwise.

After this, if the division is possible, print an example of how to create the sets. First, print the number of elements in the first set followed by the elements themselves in a separate line, and then, print the second set in a similar way.

Constraints

    1≤n≤106


Example 1

Input:
7

Output:
YES
4
1 2 4 7
3
3 5 6

Example 2

Input:
6

Output:
NO
''' 

#solution: division is possible if the sum of the array is even (sum%2=0). if it is even, because the array is sorted ascending, we can go for greedy approach. 
#loop over the elements and append them to the solution array, until the sum is equal or greater then half of the input array sum. if it is equal, return the created array and the rest of the elemetns 
# if it is greater, remove the first element of the array and put it back to the initial array ,check again. do until desired sum is reached


n = int(input())
s = (n*(n+1))/2

if s%2 == 0:
    print("YES")

    half = s/2 

    first = []
    second = []
    i = 0
    for i in range(n,0,-1):

        
        if(i<=half):
            first.append(i)
            half = half-i
        
        else:
            second.append(i)
    
    print(len(first))
    print(*first,sep=" ")
    print(len(second))
    print(*second,sep=" ")
        
else:
    print("NO")



