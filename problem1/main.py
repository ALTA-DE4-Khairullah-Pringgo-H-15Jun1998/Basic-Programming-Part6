def compare(a, b):
    pattern = ""
    for i,j in zip (a,b):
        if i !=j :
            pattern += str(i)
        else :
            pattern += str(j)
    return pattern

if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA