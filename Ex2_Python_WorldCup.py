matches = [
    ("Iran", "Spain"),
    ("Iran", "Portugal"),
    ("Iran", "Morocco"),
    ("Spain", "Portugal"),
    ("Spain", "Morocco"),
    ("Portugal", "Morocco")
]
# -------------------------------------------------------------------------------------
d = {}
for left_team, right_team in matches:
    # score = input(f"Enter score for {left_team} - {right_team} (format right-left like 2-1): ")
    # score = input({left_team} - {right_team} )
    score = input()
    left_score, right_score = map(int, score.split('-'))
    d[(left_team, right_team)] = (left_score, right_score)  # store in order of teams

# print(d)
# print("-----------------------")

# --------------------------- Creating Initial Dic for each item --------------------------------------
teams = ["Iran", "Spain", "Portugal", "Morocco"]

points = {}
goal_difference = {}
wins = {}
loses = {}
draws = {}

for team in teams:
    points[team] = 0
    goal_difference[team] = 0
    wins[team] = 0
    loses[team] = 0
    draws [team] = 0
# ----------------------------------------------------------------------------------------

for match, score in d.items():
    team1, team2 = match
    score1, score2 = score

    if score1 > score2:
        points[team1] += 3

        goal_difference[team1] += score1 - score2
        goal_difference[team2] += score2 - score1

        wins[team1] += 1
        loses[team2] += 1

    elif score1 == score2:
        points[team1] += 1
        points[team2] += 1

        # goal_difference[team1] += score1 
        # goal_difference[team2] += score2

        draws [team1] += 1
        draws [team2] += 1

    else:
        points[team2] += 3

        goal_difference[team1] += score1 - score2
        goal_difference[team2] += score2 - score1

        wins[team2] += 1
        loses[team1] += 1

# print("wins:", wins)
# print('loses:', loses)
# print("draws:", draws)
# print("goal_difference:", goal_difference)
# print("points:", points)
# --------------------------------------------------------------------------------------
teams = ["Iran", "Spain", "Portugal", "Morocco"]

team_info = [(t, points[t], wins[t], loses[t],draws[t], goal_difference[t])  for t in teams]
# print(team_info)
# print("-----------------------------------")

sorted_teams = sorted(team_info, key=lambda x: (-x[1], -x[2], x[0]))
# print("sorted_teams:", sorted_teams)

# Print in the desired format
for team in sorted_teams:
    name, points, wins, loses, draws, gd = team
    print(f"{name}  wins:{wins} , loses:{loses} , draws:{draws} , goal difference:{gd} , points:{points}")