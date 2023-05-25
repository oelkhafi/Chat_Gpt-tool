n=int(input())

def add(namespase, var):
  global d
  d[namespase].append(var) 
    
def create(what, where):
  global d
  d[what]= []
  d[where].append(d[what])
  dicts[what]=where
    
def get(where, what):
  temp=True
  global dicts
  global d
  for el in d[where]:
    #print (what , el, d[where])
    if what == el: 
      print (where)
      temp=False
  if temp and where== ""global"" and  not what in d[""global""]: print ( ""None"")
  elif temp: get(dicts[where], what)

d={}
d[""global""]=[]
dicts={}

dicts[""global""]=""stop""

for i in range(n):
  l = input().strip().split()
  if l[0]==""add"": add(l[1],l[2])  
  if l[0]==""create"": create(l[1],l[2])
  if l[0]==""get"": get(l[1],l[2]) 