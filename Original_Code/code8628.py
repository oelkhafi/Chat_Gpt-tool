def is_ancestor(cls_anc, cls_dsp, classes):
    if cls_anc in classes[cls_dsp] or cls_anc == cls_dsp:
        return True
    else:
        for cls in classes[cls_dsp]:
            if is_ancestor(cls_anc, cls, classes): return True
    return False
            
inh_data = [input().replace(':','').split() for i in range(int(input()))]
qry_data = [[input(), True] for i in range(int(input()))]
classes = {}
for elm in inh_data:
    classes[elm[0]] = []
    for i in range(1,len(elm)):
        classes[elm[0]].append(elm[i])  
if len(qry_data) > 1:    
    for i in range((len(qry_data)-1),0,-1):
        for j in range(i-1, -1,-1):
            if is_ancestor(qry_data[j][0],qry_data[i][0], classes):
                qry_data[i][1] = False
                break
[print(elm[0]) for elm in qry_data if elm[1] == False] 