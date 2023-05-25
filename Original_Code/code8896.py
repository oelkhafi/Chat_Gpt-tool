# put your python code here
alf = input()
res_alf = input()

encode = input()
decode = input()

code = {}
decrypt = {}
for i in range(len(alf)):
    code.update([(alf[i], res_alf[i])])
    decrypt.update([(res_alf[i], alf[i])])


res_encode = []
for letter in encode:
    res_encode.append(code[letter])

print(''.join(res_encode))

res_decode = [decrypt[let] for let in decode]
print(''.join(res_decode))





 