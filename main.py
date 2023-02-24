import random
import csv

players = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']

game_result = []
for player in players:
    for i in range(10):
        score = random.randint(0,100)
        game_result.append([player,score])
        
with open ('game_results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Player name', 'Score'])
    for result in game_result:
        writer.writerow(result)