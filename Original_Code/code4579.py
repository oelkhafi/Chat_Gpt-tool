# для Вашего удобства словарь вида ""буква: код Морзе"" уже готов
morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••', 'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—', 'r': '•—•', 's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—', 'y': '—•——', 'z': '——••'}
def convert(d, x):
    if x in d.keys():
        return d[x]
    for a, b in d.items():
        if b == x:
            return a

result = ''
string = input().lower()
if '—' not in string and '•' not in string:
    for counter in range(len(string) - 1):
        if string[counter] != ' ':
            result += convert(morze, string[counter])
            if string[counter + 1] != ' ':
                result += ' '
        else:
            result += '\t'
    result += convert(morze, string[-1])
else:
    buffer = string.split('\t')
    for counter in buffer:
        for counter2 in counter.split():
            result += convert(morze, counter2)
        result += ' '
print(result)
 