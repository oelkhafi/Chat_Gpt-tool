# put your python code here

gen = input()
part = """"
letter = """"
code = """"
w = 1
c = 0
for i in gen:
    c += 1
    try:
        if i == gen[c]:
            w += 1
        else:
            part = i + str(w)
            code = code + part
            w = 1
    except IndexError:
        part = i + str(w)
        code = code + part
print(code)


 