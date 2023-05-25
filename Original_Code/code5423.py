def update_result(name, team, goals1, goals2):
    match_result = [1,
                    1 if (goals1 > goals2) else 0,
                    1 if (goals1 == goals2) else 0,
                    1 if (goals1 < goals2) else 0,
                    3 if (goals1 > goals2) else 1 if (goals1 == goals2) else 0
    ]
    return {team: match_result} if name is None \
        else {team: [a + b for a, b in zip(name, match_result)]}


table = {}
for _ in range(int(input())):
    matches = input().strip().split(';')
    table.update(update_result(table.get(matches[0]),
                               matches[0],
                               matches[1],
                               matches[3]
    ))
    table.update(update_result(table.get(matches[2]),
                               matches[2],
                               matches[3],
                               matches[1]
    ))

for team_name, total in table.items():
    print(f'{team_name}:', *total)
 