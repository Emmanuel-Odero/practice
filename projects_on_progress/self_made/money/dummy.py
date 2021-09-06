'''#this is just a dummy file to generate values to our members database

from faker import Faker


# below we will use faker module to generate dummy data to used to fill our database 

faker = Faker()

names = []
for x in range(10000):
	name = faker.last_name()
	names.append(name)


unique_names = set(names)


#definae a funtion which  adds the generated dummy list as members
import sqlite3
import random

db = sqlite3.connect('./site.db')

#a function that adds the dummy user data to the database.
def insert_record(my_link, username, joining_link):
	db.execute(''' INSERT INTO members(my_link, username, joining_link)
		VALUES(?,?,?) ''', (my_link, username, joining_link))

	db.commit()

def add_member(name):

	#list all the used links and know which to give next
	used_links_list = []
	used_links = db.execute("SELECT * FROM members")
	for link in used_links:
		used_links_list.append(link[0])

	#from the already used links determine the link for the new user
	number_to_issue = len(used_links_list) + 1
	next_link_for_issue = f'www.{str(number_to_issue).zfill(5)}'

	used_links_list.remove('www.00001')  #we remove the super user giving us ability to choce from the other members
	joining_link = random.choice(used_links_list)

	insert_record(next_link_for_issue, name, joining_link)

	return print(f"{next_link_for_issue} added")

print(len(unique_names))

for name in unique_names:
	add_member(name)'''