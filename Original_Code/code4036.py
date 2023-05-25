n = int(input())
if n in([11,111,211,311,411,511,611,711,811,911,1111,12,112,
         212,312,412,512,612,712,812,912,1112,13,113,
         213,313,413,513,613,713,813,913,1113,14,114,214,
         314,414,514,614,714,814,914,1114]):
    
    print('{0} программистов'.format(n))

elif n in [i for i in range(1,1000,10)]:
    print('{0} программист'.format(n))
    
elif n in [i for i in range(2,1000,10)]:
    print('{0} программиста'.format(n))
    
elif n in [i for i in range(3,1000,10)]:
    print('{0} программиста'.format(n))
elif n in [i for i in range(4,1000,10)]:
    print('{0} программиста'.format(n))
else:
    print('{0} программистов'.format(n))
 