def add_league():
	league_name = input(f"League name to be Added : ")
	leagues.append(league_name)
	league_index = leagues.index(league_name)

	return f"{league_name} has been added with number {league_index}"

print("Welcome To Soccer World\n")

leagues = ["epl", "bundersliga"]


print(f"Select League for Analysis.")
for i, league in enumerate(leagues):
	print(f"{i} : {league}")

#request user to input the league of choice
league_choice = int(input("\nLeague No : "))

current_league = leagues[league_choice]
print(current_league)

