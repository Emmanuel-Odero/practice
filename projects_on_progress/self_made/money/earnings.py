import sqlite3

db = sqlite3.connect("./site.db")

query_link = input("Input your link to know your balance : ")


user = {} #this dictionary saves db queries about the user in question
user_details =db.execute("SELECT * FROM members WHERE my_link=?", (query_link, ))
for details in user_details:
	user['my_link'] = details[0]
	user['username'] = details[1]
	user['joining_link'] = details[2]

#concerning the user we creates lists of the first to the third referals
first_referals_list = []
second_referals_list = []
third_referals_list = []


first_referals = db.execute("SELECT * FROM members WHERE joining_link=?", (query_link, ))
for first in first_referals:
	first_referals_list.append(first[0])

for link in first_referals_list:
	second_referals = db.execute("SELECT * FROM members WHERE joining_link=?", (link, ))
	for second in second_referals:
		second_referals_list.append(second[0])

for link in second_referals_list:
	third_referals = db.execute("SELECT * FROM members WHERE joining_link=?", (link, ))
	for third in third_referals:
		third_referals_list.append(third[0])


print(f'First referals : {first_referals_list}\n')
print(f'Second referals : {second_referals_list}\n')
print(f'Third referals : {third_referals_list}\n')


#based on the lists above we compute the user earnings
print(f"Dear {user['username']}, you have {len(first_referals_list)} first referals, {len(second_referals_list)} second referals and {len(third_referals_list)} third referals.")
total_earnings = (len(first_referals_list) * 300) + (len(second_referals_list) * 100) + (len(third_referals_list) * 50)
print(f"Your earnings amount to : {total_earnings}")