'''
Your task is to count for k=1,2,…,n the number of ways two knights can be placed on a k×k chessboard so that they do not attack each other.

Input

The only input line contains an integer n.

Output

Print n integers: the results.

Constraints

    1≤n≤10000


Example

Input:
8

Output:
0
6
28
96
252
550
1056
1848'''


k = int(input())
for n in range(1,k+1):
    import math
    #total number of ways to set 2 pieces on a chessboard minus number of positions two knights attack each other 
    res = n * n * (n * n - 1) / 2 - 4 *(n-1)*(n-2)
    print(int(res))

