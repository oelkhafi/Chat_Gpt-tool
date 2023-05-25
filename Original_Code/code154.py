games, wins, draw, lost = {}, {}, {}, {}
for i in range(int(input())):
    a, aScore, b, bScore = input().split(';')
    aScore, bScore = int(aScore), int(bScore)
    games[a], games[b] = games.get(a, 0) + 1, games.get(b, 0) + 1
    draw[a], draw[b] = draw.get(a, 0), draw.get(b, 0)
    wins[b], wins[a] = wins.get(b, 0), wins.get(a, 0)
    lost[a], lost[b] = lost.get(a, 0), lost.get(b, 0)
    if aScore == bScore:
        draw[a] = draw.get(a, 0) + 1
        draw[b] = draw.get(b, 0) + 1
    elif aScore > bScore:
        wins[a] = wins.get(a, 0) + 1
        lost[b] = lost.get(b, 0) + 1
    elif aScore < bScore:
        wins[b] = wins.get(b, 0) + 1
        lost[a] = lost.get(a, 0) + 1
for i in games.keys():
    print(i, ':', sep='', end='')
    print(*[games[i], wins[i], draw[i], lost[i], wins[i] * 3 + draw[i]])
 