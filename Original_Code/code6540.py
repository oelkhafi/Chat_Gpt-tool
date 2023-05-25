import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def staircase(nums):    
    n = len(nums)
    if n == 1:       
        return max(0, nums[0])
    elif n == 2:        
        return max(nums[0], nums[1], nums[0] + nums[1])
    else:
        s_1 = staircase(nums[:-1])
        s_2 = staircase(nums[:-2])
        return max(nums[-1] + s_1, nums[-2] + s_2)
    

def main():   
    _ = int(next(sys.stdin))
    nums = list(map(int, next(sys.stdin).split()))
    nums = tuple([0] + nums)  
    print(nums[-1] + staircase(nums[:-1]))


if __name__ == ""__main__"":
    main()
 