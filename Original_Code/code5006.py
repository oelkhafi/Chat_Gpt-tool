c_min = 0
p = int(input())
if p != 0:
	cnt = 1
while p != 0:
    t = int(input())
    if t == p:
        cnt += 1
    else:
    	if c_min == 0:
    		c_min = cnt
    		cnt = 1
    		p = t
    	else:
    		if c_min > cnt:
    			c_min = cnt
    			cnt = 1
    			p = t
    if t == 0:
    	break
print(c_min) 