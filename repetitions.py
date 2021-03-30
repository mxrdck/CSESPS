'''
ou are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.

Input

The only input line contains a string of n characters.

Output

Print one integer: the length of the longest repetition.

Constraints

    1≤n≤106


Example

Input:
ATTCGGGA

Output:
3'''


dna = input()

dna_len = len(dna)
lrep = 1
n = 0
while (n < len(dna)-1):
        
    curr = dna[n] 
    
    i = n+1
    curr_rep = 1
    while(i <= len(dna)-1):
        nxt = dna[i]
        if curr == nxt:
            curr_rep += 1 
            i +=1 
            n = i
        else:
            n = i
            break
    
    lrep = max(curr_rep, lrep)


print(lrep)
