


#palindrome examples:
'''
    ABA
    AA
    ACCA
    AACBCAA
'''
#random strings:
'''
AAABBB
'''

def count_chars(pal:str):
    counts = {}
    for char in pal:

        if char in counts.keys():
            counts[char] +=1 
        else:
            counts[char] = 1 
    return counts


def pal_possible(charcounts:dict):
    has_odd = False

    for val in charcounts.values():
        
        if val % 2 != 0:
            if has_odd == False:
                has_odd = True
            else:
                return False
    
    return True

def create_pal(charcounts:dict):
    pal = ""

    sorted_chars = {k: v for k, v in sorted(charcounts.items(), key=lambda item: item[1], reverse=True)}
    stash = ""
    for char in sorted_chars.keys():
        charcount = sorted_chars[char]

        if charcount % 2 == 0:
            pal = pal + char *(charcount // 2)
        else:
            stash = char*charcount

    pal = pal+stash

    for char in list(sorted_chars.keys())[::-1]:
         charcount = sorted_chars[char]
         if charcount % 2 == 0:
            pal = pal + char *(charcount // 2)


    return pal




pal = input()

counts = count_chars(pal)
if pal_possible(counts):
    print(create_pal(counts))
else:
    print("NO SOLUTION")