def end_game(game_result):
    if game_result:
           #print('Вводим результаты игр:')
           result=input().split(';')
           table(result[0], int(result[1]),int(result[3]))
           table(result[2], int(result[3]),int(result[1]))
           game_result-=1
           end_game(game_result)
def table(a,b,c,):
    if a not in spisok:
        spisok[a] = [0, 0, 0, 0, 0]
    spisok[a][0] += 1
    if b > c:
        spisok[a][1] += 1
        spisok[a][4] += 3
    elif c > b:
        spisok[a][3] += 1
    else:
        spisok[a][2] += 1
        spisok[a][4] += 1
def print_game():
    for key,value in spisok.items():
        print(key,end =':')
        print(value[0],value[1],value[2],value[3],value[4])
spisok ={}
#print('Вводим количестов сыгранных игр:')
end_game(int(input()))
print_game()
 