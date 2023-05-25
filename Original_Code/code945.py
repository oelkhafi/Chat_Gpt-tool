# put your python code here
def main():
    n, m  = map(int,input().split())
    life_field = [] 
    for _ in range(n):
        life_field.append(input())
    second_gen = []
    for i in range(n):
        s = ''
        for j in range(m):
            s+=status_point(i, j, life_field)            
        second_gen.append(s)
            
    print('\n'.join(i for i in second_gen))

def status_point(ind_i,ind_j,mx):
    n = len(mx)
    m = len(mx[0])
    neib_status = {'.':0 , 'X':1 }
    neib_count = 0
    for i in range(ind_i-1, ind_i+2):
        for j in range(ind_j-1, ind_j+2):
            if i == ind_i and j == ind_j: continue
            neib_count += neib_status[mx[(i+n)%n][(j+m)%m]]
    if mx[ind_i][ind_j] == '.': #if dead
        if neib_count == 3: return 'X'
        else: return '.'
    else: #if alive
        if 2 <= neib_count <= 3: return 'X'
        else: return '.'    

if __name__ == ""__main__"": main() 