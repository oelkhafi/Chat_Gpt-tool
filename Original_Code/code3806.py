n=int(input()) #obtaining the number of games
games=[]
for c in range(n): #recording scores for games
    game=[int(i) if i.isnumeric() else i for i in input().split(';')] #scores are converted to integers at input
    games.append(game) #each game is in a separate sublist
res={} #new dict for results
for game in games:
    for i in (0,2): #selecting only teams' names in each sublist
        if game[i] not in res: #adding teams if they are not in the dict
            res[game[i]]=[0,0,0,0,0]
        res[game[i]][0]+=1 #counting games played
        if game[i+1]>game[i-1]: 
            res[game[i]][1]+=1 #counting wins
            res[game[i]][4]+=3 #adding points for a win
        elif game[i+1]==game[i-1]:
            res[game[i]][2]+=1 #counting draws
            res[game[i]][4]+=1 #adding points for a draw
        else:
            res[game[i]][3]+=1  #counting losses
for key, value in res.items():
    print(key+':',*value)



 