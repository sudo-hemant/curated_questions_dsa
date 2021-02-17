
def bit_anagram(a, b):

    while a and b:
        a = a & (a - 1)
        b = b & (b - 1)
    
    if a or b:
        return False
    return True


print(bit_anagram(4, 5))