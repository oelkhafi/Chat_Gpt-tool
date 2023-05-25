import requests
import re
str1 = input()
str2 = input()
d = False
a = requests.get(str1).text
if requests.get(str1).status_code == 200:
    for i in re.findall(r'''<a href=['""](.*?)['""]''',a):
 
            
        j = requests.get(i).text
        if requests.get(i).status_code == 200:
            for k in re.findall(r'''<a href=['""](.*?)['""]''',j):
                if k == str2:
                    d = True
if d == True:
    print('Yes')
else:
    print('No')
            
      
                
            
        
        

 