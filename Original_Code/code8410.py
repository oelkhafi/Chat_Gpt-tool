from functools import lru_cache


@lru_cache(maxsize=None)
def edit_distance(A, B):
    if len(A) > len(B):
        A, B = B, A
    i = 0
    while i < len(A) and A[-i-1] == B[-i-1]:
        i += 1
    A, B = A[:len(A)-i], B[:len(B)-i]
    if not A or not B: 
        return len(A) + len(B)
    temporary_result = edit_distance(A[:-1], B) + 1
    temporary_result = min(temporary_result, edit_distance(A, B[:-1]) + 1)
    temporary_result = min(temporary_result, edit_distance(A[:-1], B[:-1]) + 1)
    return temporary_result


print(edit_distance(input(), input()))
 