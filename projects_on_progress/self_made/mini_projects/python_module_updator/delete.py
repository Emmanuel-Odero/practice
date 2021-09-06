import os

modules = []

with open('cleaned_modules.txt') as f:
	lines = f.readlines()
	for line in lines:
		if line != '\n':
			modules.append(line[:-2])

for module in modules:
	command = f"pip install {module}"
	os.system(command)

	