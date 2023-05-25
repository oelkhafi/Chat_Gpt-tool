import requests

import re

def search_url(A, B):
    res_A = requests.get(A)
    content_tipe_A = res_A.headers['Content-Type']

    if res_A.status_code == 200 and content_tipe_A.find('text') != -1:
        pattern = r""<a.*href=\""(.*)\""""

        for i in re.findall(pattern, res_A.text):
            res_B = requests.get(i)
            content_tipe_B = res_B.headers['Content-Type']

            if res_B.status_code == 200 and content_tipe_B.find('text') != -1:

                for j in re.findall(pattern, res_B.text):
                    if j == B:
                        print('Yes')
                        return
                    
    print('No')



A = input().strip()
B = input().strip()
search_url(A, B)
 