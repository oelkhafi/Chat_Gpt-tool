# put your python code here
s = input()
a = input()
b = input()

counter = 0

def replaceText(text):
    global counter
    if (a in b) and (a in text):
        return False
    elif counter <= 1000:
        if a not in text and a in b:
            return True
        else:        
            replacedText = text.replace(a, b)
            counter += 1
            if a in replacedText:
                res = replaceText(replacedText)
                if res is True:
                    return True
            else:
                return True
    else:
        return False                        
res = replaceText(s)
    
if res is True:
    print(counter)
else:
    print(""Impossible"") 