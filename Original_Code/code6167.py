def letter_to_morse(s):
    morse_word = []
    s = s.split()
    for word in s:        
        list(word)
        word_m = []
        for i in range(len(word)):                        
            word_m.append(book.get(word[i]))
        word_m = ' '.join(word_m)        
        morse_word.append(word_m)
    return('	'.join(morse_word))
     
    

def morse_to_letter(s):
    morse_word = []
    s = s.split('	')
    for word in s:
        word = word.split(' ')
        word_m = []
        for i in range(len(word)):                    
            for key, value in book.items():
                if value == word[i]:
                    word_m.append(key)
        word_m = ''.join(word_m)            
        morse_word.append(word_m)            
    return(' '.join(morse_word))        



book = {'a' : '•—','b' : '—•••','c' : '—•—•','d' : '—••','e' : '•', 'f' : '••—•','g' : '——•','h' : '••••',
        'i' : '••','j' : '•———','k' : '—•—','l' : '•—••','m' : '——','n' : '—•','o' : '———',
        'p' : '•——•','q' : '——•—','r' : '•—•','s' : '•••','t' : '—','u' : '••—','v' : '•••—',
       'w' : '•——','x' : '—••—','y' : '—•——','z' : '——••'}

sw = input().lower()
if sw[0].isalpha():    
    print(letter_to_morse(sw))
else:
    print(morse_to_letter(sw))
 