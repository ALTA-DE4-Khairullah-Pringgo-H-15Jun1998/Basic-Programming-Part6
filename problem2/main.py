def caesar(offset, input_str):
    teks_eknkripsi = ""
    for x in input_str:
        if 96 < ord(x) < 123:
            teks_eknkripsi += chr((ord(x)+offset-97)%26+97)
        else:
            teks_eknkripsi += x
    return teks_eknkripsi

if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl