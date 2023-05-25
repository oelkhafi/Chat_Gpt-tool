def return_key(dict1, value):
    for jb in dict1.keys():
        if dict1[jb] == value:
            return jb


alphabet = input()
cipher = input()
cipher_key = {}
z = 0
for i in alphabet:
    cipher_key[i] = cipher[z]
    z += 1
for i in range(2):
    text1 = input()
    for j in range(len(text1)):
        if i == 0:
            print(cipher_key[text1[j]], end='')
            if j == len(text1) - 1:
                print()
        else:
            print(return_key(cipher_key, text1[j]), end='')
 