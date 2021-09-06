def remover(name):
	try:
		end = name.index('=')
	except:
		end = name.index('@')
	name = name[0:end]
	return name

filename = input("Input filename containing modules :")
file = open(filename, encoding='utf-8')
module_list = file.readlines()
file.close()

modified_list = []
for module in module_list:
	module = remover(module)
	modified_list.append(module)

#now using the modified_list we write to a file line by line
import os

with open('./cleaned_modules.txt', 'a') as f1:
	for module in modified_list:
		f1.write(module + os.linesep)