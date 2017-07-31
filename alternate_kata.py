def is_alt(s):
    vowel = ['a', 'e', 'i', 'o', 'u']
    cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    lst= []

    for i in range(len(s)):
        if (s[0] in vowel and ((i % 2 == 0 and s[i] in vowel) or (s[i] in cons and i % 2 != 0))): 
            lst.append('True')
        elif (s[0] in cons and ((i % 2 == 0 and s[i] in cons) or (s[i] in vowel and i % 2 != 0))): 
            lst.append('True') 
        else:
            lst.append('False')
    return 'False' if 'False' in lst else 'True'
    

print(is_alt("amazon")) #, True)
print(is_alt("apple")) #, False)
print(is_alt("banana")) #, True)
print(is_alt("orange")) #, False)
print(is_alt("helipad")) #, True)
print(is_alt("yay")) #, True)

