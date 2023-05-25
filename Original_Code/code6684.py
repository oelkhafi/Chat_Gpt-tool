import json

d = {}
d_out = {}

data = json.loads(input())

for el in data:
    d[el[""name""]] = el[""parents""]
    d_out[el[""name""]] = set()

    



    
    
def add_all_child (current, parent, d, d_out):
    for  element in d.keys():
        if parent in d[element]:
            d_out[current].add(element)
            add_all_child (current, element, d, d_out)
    
            
for name in sorted(d.keys()):
    current = name
    add_all_child (current, name, d, d_out)  
    print (name, len(d_out[name])+1, sep ="" : "" )

    






 