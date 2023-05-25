x = input()
S, single, double = str(), str(), str()
cnt = 1
prev = x[0]

if len(x) == 1:
    print(x+'1')
else:
    for i in x[1:]:
      if prev == i:
        cnt += 1
        double = prev+str(cnt)
        single = str()
      else: 
          if double != """":
              cnt = 1
              prev = i
              single = prev + '1'
              S = S + double
              double = str()
              continue
          else:
            cnt = 1
            single = prev + '1' 
            S = S + double + single
            single = i + '1'
            prev = i

print(S+double+single)
     