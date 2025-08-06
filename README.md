# 🏆 World Cup Group B Ranking Calculator

This Python script calculates and displays the final rankings of four teams in **Group B** of the World Cup based on their match results.

The teams included are: **Iran**, **Spain**, **Portugal**, and **Morocco**.

---

## 📌 Problem Statement

Write a Python program that:

- Accepts the results of 6 matches between the 4 teams
- Calculates for each team:
  - Number of wins, losses, and draws
  - Goal difference (goals scored minus goals conceded)
  - Total points

Each team's data is printed on a separate line, **sorted** by:

1. **Points (descending)**
2. **Wins (descending)**
3. **Alphabetical order (ascending)**

---

## 📥 Input Format

- The program expects 6 inputs — one for each match.
- Each input is a string in the format:  
  X-Y
  Where `x` is the number of goals scored by the **right-side team**, and `y` is the number of goals scored by the **left-side team**.

### Match order:
Iran - Spain
Iran - Portugal
Iran - Morocco
Spain - Portugal
Spain - Morocco
Portugal - Morocco

> 📌 Example input:
2-2
1-2
3-1
2-2
3-1
3-1
> 
---

## 📤 Output Format

Each team is printed in its own line:

Teams are ordered by:
- Total points (highest first)
- If tied: more wins
- If still tied: alphabetically

> 📌 Example output:
Spain wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
Iran wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Portugal wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Morocco wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3
