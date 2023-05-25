DIGITS = {'I' : 1,
          'V' : 5,
          'X' : 10,
          'L' : 50,
          'C' : 100,
          'D' : 500,
          'M' : 1000,
         }

s = input()
r = 0
for i, c in enumerate(s):
        k = i + 1
        if len(s) == k or DIGITS[c] >= DIGITS[s[k]]:
            r += DIGITS[c]
        else:
            r -= DIGITS[c]
print(r)





 