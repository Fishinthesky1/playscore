import csv

game_results = []
with open ('game_results.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        game_results.append(row)
        
high_scores = {}
for result in game_results:
    player = result[0]
    score = int(result[1])
    if player not in high_scores:
        high_scores[player] = score
    else:
        if score > high_scores[player]:
            high_scores[player] = score
            
sort_players = sorted(high_scores.items(), key=lambda x:x[1], reverse=True)

with open('high_scores.csv', 'w', newline ='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Player name', 'Best result'])
    for player, score in sort_players:
        writer.writerow([player, score])