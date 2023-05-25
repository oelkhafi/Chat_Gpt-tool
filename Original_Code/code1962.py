def split_encode_series(string):
  a = string + '.'
  res = []
  count = 1
  for i in range(len(a)-1):
    if (a[i] != a[i+1]):
      res.append((count, a[i]))
      count = 1
    else: count += 1
  return res
  
def final_result(list):
  res = list
  final = ''
  for i in range(len(res)):
    if (res[i][0] == 1):
      final += res[i][1]
    else:
      final += str(res[i][0]) + res[i][1]
  return final

res = split_encode_series(input())
print(final_result(res))
 