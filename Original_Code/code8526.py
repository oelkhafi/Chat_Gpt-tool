# put your python code here
dictionary = []
for i in range(int(input())):
    j = input().lower()
    dictionary.append(j)

text = []
for i in range(int(input())):
     j = input().lower().split()
     for l in j:
         text.append(l)

errors = []
for i in text:
    if (i not in errors and i not in dictionary):
        errors.append(i)
for i in errors:
    print(i)



 