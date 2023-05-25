import json


def aloha(voc1, voc2):
    for k0 in voc1.keys():
        for k1 in voc1.keys():
            if k0 in voc1[k1]:
                voc2[k0].append(k1)


voc, ouf = {}, {}
p_file = json.loads(input())
for i in p_file:
    voc[i['name']] = i['parents']
for i in sorted(voc):
    ouf[i] = []

aloha(voc, ouf)


def find(vocab):
    for key in vocab.keys():
        for e in vocab[key]:
            if e in vocab.keys():
                vocab[key].extend(vocab[e])


find(ouf)

for i in ouf.keys():
    ouf[i] = len(set(ouf[i])) + 1

for k, v in ouf.items():
    print(k + ' : ' + str(v), end='\n')
 