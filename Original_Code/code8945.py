ltype = input()
if ltype == ""int"":
    a = int(input())
    b = int(input())
    if a or b: print(a + b)
    else: print(""Empty Ints"")
elif ltype == ""str"":
    a = input()
    if a: print(a)
    else: print(""Empty String"")
elif ltype == ""list"":
    a = input().split()
    if a: print(a[-1])
    else: print(""Empty List"")
else: print(""Unknown type"")
  




 