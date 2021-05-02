'''
wikipedia: 
The binary-reflected Gray code list for n bits can be generated recursively from the list for n − 1 bits by reflecting the list (i.e. listing the entries in reverse order), prefixing the entries in the original list with a binary 0, prefixing the entries in the reflected list with a binary 1, and then concatenating the original list with the reversed list.[12] For example, generating the n = 3 list from the n = 2 list:
2-bit list: 	00, 01, 11, 10 	 
Reflected: 	  	10, 11, 01, 00
Prefix old entries with 0: 	000, 001, 011, 010, 	 
Prefix new entries with 1: 	  	110, 111, 101, 100
Concatenated: 	000, 001, 011, 010, 	110, 111, 101, 100 
'''

def gray_code(gc:int):
    
    if gc==0:
        return [""]
    else:
        
        gc = gray_code(gc-1)

        reflected = gc[::-1]
        old_prefixed = ["0"+ x for x in gc]
        new_prefixed = ["1"+x for x in reflected]

        return old_prefixed + new_prefixed



n = int(input())
print(*gray_code(n), sep="\n")