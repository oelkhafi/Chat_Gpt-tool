# put your python code here
size,n = [int(x) for x in input().split()]
if size == 0:
    for i in range(n):
        print(-1)
elif n>=0:
    cur_time = 0
    buf = []
    cur_pos = 0
    buf_time = 0
    if size >= n:
        for i in range(n):
            a,d=[int(x) for x in input().split()]
            print(max(a,cur_time))
            cur_time = max(a,cur_time) + d
    else:
        for i in range(size):
            a,d=[int(x) for x in input().split()]
            print(max(a,cur_time))
            cur_time = max(a,cur_time) + d
            buf.append((a,d))
        for i in range(size,n):
            a,d=[int(x) for x in input().split()]
            if buf[cur_pos][1] + max(buf_time,buf[cur_pos][0]) > a:
                print(-1)
            else:
                print(max(a,cur_time))
                cur_time = max(a,cur_time) + d
                buf_time = max(buf_time,buf[cur_pos][0]) + buf[cur_pos][1]
                buf[cur_pos]=(a,d)
                cur_pos = (cur_pos + 1)%size



 