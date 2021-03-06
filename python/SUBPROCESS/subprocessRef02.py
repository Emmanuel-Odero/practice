import subprocess

subprocess.run('dir', shell=True) #shell equalling to true only applies to windows since without it an error is poped out but can be a security hazard
#subprocess.run(['start', 'powershell'])  #note that without using the the shell argument we have to use a list of strings as commands

#we can save this commands to a variable then when we print we get a completed process object that we can use as follows
p1 = subprocess.run('start powershell', shell=True)
print(p1)

#print(p1) #This shows use the command we passed.
#print(p1.returncode) #gives the state of return code 0=sucesses, 

#to capture the output to a variable
p2 = subprocess.run('netsh wlan show networks', capture_output=True, text=True) 
print(p2.stdout) #this is a byte output
#print(p2.stdout.decode()) #Here we decode the bytes to string but we can avoid this by using text=True in the subprocess

justExampleofTextOutput = subprocess.run('netsh wlan show networks', capture_output=True) 

#what the capture_output=True is actually doing in the background is setting stdout and stderr the subproces pipe
#so in replace of capture we can use stdout = subprocess.PIPE

#to write into a file we can do something like this
with open('output.txt', 'w') as f:
	p3 = subprocess.run('type *.py', shell=True, stdout=f, text=True)

#note that we pass a commad to a variable and its and error then we can check it by using the return code which will
#be 0 for success and 1 for an error.so if we wanted to run our code if only that command was a succes then we can use
# if p3.returncode != 0: then the condition if it dint work. then if we want to see that error we can type p3.stderr. A

#NOTE that if we wanted to see the error then we can use check=True to see the error in full.	

#now if we wanted to take an output of one command to be the imput to another

p4 = subprocess.run('dir', capture_output=True, text=True, input=p1.stdout) #doesn.t work in this case of the logic used