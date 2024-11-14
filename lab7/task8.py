scoreboard = input("Введите надпись: ")

teams, score = scoreboard.rsplit(" ", 1)

team = teams.split("-")
score = score.split(":")

if int(score[0]) > int(score[1]):
    print(team[0])
elif int(score[0]) < int(score[1]):
    print(team[1])
else:
    print("Ничья")