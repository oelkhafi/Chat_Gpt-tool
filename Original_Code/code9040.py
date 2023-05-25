import json
class Pear():
    
    def __init__(self):
        self.dic = {}
        self.lstp = []
        self.fl = False
    def add(self, instr):
        w = instr.strip().split(':')
        if len(w) == 1:
            self.dic[w[0].strip()] = []
        else:
            self.dic[w[0].strip()] = w[1].strip().split()
    
    def ifpear(self, lst):
        self.fl = False
        self.ifpear1(lst)
        return self.fl
    
    def ifpear1(self, lst) -> bool:
        if lst[0] and lst[1] in self.dic:
            if lst[0] == lst[1] or lst[0] in self.dic[lst[1]]:
                self.fl = True
            else:
                for eny in self.dic[lst[1]]:
                    self.ifpear1([lst[0],eny])
                    
    def pearcnt(self, ind) -> str:
        cnt = 0
        if ind < len(self.lstp):
            valind = self.lstp[ind]
            for i in self.lstp:
                if self.ifpear([valind, i]):
                    cnt += 1
        return str(cnt)

pp = json.loads(input())
a = Pear()
[a.add(pp[_].get(""name"") + "" : "" + ' '.join(pp[_].get(""parents""))) for _ in range(len(pp))]
s = [i for i in a.dic.keys()]
[s.extend(j) for j in a.dic.values()]
a.lstp.extend(sorted(list(set(s))))
[print(a.lstp[_] + "" : "" + a.pearcnt(_)) for _ in range(len(a.lstp))]



 