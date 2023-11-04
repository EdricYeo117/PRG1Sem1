player = ['Hafu', 'Toast', 'Pokimane', 'Pewdiepie', 'Ninja', 'Markiplier']
results = [ [98, 107, 87, 121], [88, 111], [79, 130, 99], [86, 100, 121, 66, 98], [108, 79, 92], [77, 126, 93, 100, 73, 89] ]
details = []
    
for logs in results:
    person  = []
    games = 0
    wins  = 0
    total = 0
    games = len(logs)
    for score in logs:
        if score >= 100:
            wins += 1
        total += score
    person += [games] + [wins] + [total]
    details += [person]

print("{:13}{:5}{:>5}{:^7}".format('Player', 'Games', 'Wins', 'Total'))

for i in range(len(player)):
    print("{:13}{:^5}{:^5}{:^7}".format(player[i], details[i][0], details[i][1], details[i][2]))
