import sqlite3

db = sqlite3.connect('./site.db')

#list all the used links and know which to give next
used_links_list = []


used_links = db.execute("SELECT * FROM members")

for link in used_links:
	used_links_list.append(link[0])

#from the already used links determine the link for the new user
number_to_issue = len(used_links_list) + 1
next_link_for_issue = f'www.{str(number_to_issue).zfill(5)}'

my_link = next_link_for_issue
joining_link = input("Input the link you are joining with :")
username = input("Input the username you would like to use :")

#insert the new user to the database
def insert_record(my_link, username, joining_link):
	db.execute(''' INSERT INTO members(my_link, username, joining_link)
		VALUES(?,?,?) ''', (my_link, username, joining_link))

	db.commit()

if joining_link not in used_links_list:
	print("\nThe link does not exist, please join with a viable link")
else:
	insert_record(my_link, username, joining_link)

print(f"{username} you have been succefully been added to the money game and your link is {my_link}")





