from collections import Counter


def countWords_Counter(s):
  return Counter(s.split())


def countWords(s):
    res = {}
    for word in s.split():
      if word in res:
        res[word] += 1
      else:
        res[word] = 1
        
    return res


res = countWords(input().strip().lower())
print(""\n"".join(map(lambda x: str(x) + "" "" + str(res[x]), res)))
 