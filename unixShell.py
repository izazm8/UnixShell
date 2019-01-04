import os

def printDirectories(dirsAndFiles,breakPoint):
	if len(dirsAndFiles) == 0:
		print(end='')
	else:
		for i in sorted(dirsAndFiles):
			if i[0]!='.':
				print(i, end=breakPoint)
		print()

def printReverseDirectories(dirsAndFiles,breakPoint):
	if len(dirsAndFiles) == 0:
		print(end='')
	else:
		for i in sorted(dirsAndFiles,reverse=True):
			if i[0]!='.':
				print(i, end=breakPoint)
		print()

def printAllDirectories(dirsAndFiles,breakPoint):
	if len(dirsAndFiles) == 0:
		print(end='')
	else:
		for i in sorted(dirsAndFiles):
			print(i, end=breakPoint)
		print()

def goBehind(cmd):
	count=1
	for i in reversed(cmd[:-1]):
		if i == "/":
			break;
		count=count+1
	return cmd[:-count]

def lsCommand(cmd, A,switch):
	if cmd[len(cmd)-1] != "/":
		cmd+='/'
	#A[cmd].sort()
	# print(t)
	# print("hi")
	if switch==-1:
		printDirectories(t,'\n')
	else:
		printDirectories(t,'   ')

def pwdCommand(curPath):
	print(curPath)

def cdCommand(cmd, curPath, A):
	#cd / #cd .. #cd ~ #cd anyPathInTheDirectry
	if cmd == ".." and curPath != "/":
		curPath=goBehind(curPath)
	elif cmd == "/":
		curPath="/"
	elif cmd == "~":
		curPath="/home/izazm8/"
	else:
		temp = curPath
		if '.' in cmd:
			print("Not a Directory")
			return curPath

		dirs=cmd.split('/')
		for d in dirs:
			check = False
			for a in A[temp]:
				if a == d:
					temp += d+"/"
					check = True
					break
			if not check:
				print("No Such Directory")
				break

		curPath=temp
		#curPath=cmd
	return curPath 
		

def helpCommand(cmd):
	lsHelps = "Usage: ls [OPTION]... [FILE]...\nList information about the FILEs (the current directory by default).\n"
	lsHelps += "Mandatory arguments to long options are mandatory for short options too.\n  -a,               do not ignore entries starting with .\n"
	lsHelps +=  "  -r,               reverse order while sorting\n"
	lsHelps +=  "  -1                list one file per line.\n\n"
	
	cdHelp = "cd: cd [~] [..] [dir]\n   Change the shell working directory.\n\nChange the current directory to DIR.  The default DIR is the value of the HOME shell variable\n\n"
	
	pwdHelp = "pwd: pwd\n    Print the current working directory\n\n"	

	if cmd[0]=='ls':
		print(lsHelps)
	elif cmd[0]=='pwd':
		print(pwdHelp)
	elif cmd[0]=='cd':
		print(cdHelp)

	# print('Hello')


#f = open("tree1.txt","w")
A = {}
startPoint = '/home/izazm8'
for root, dirs, files in os.walk(startPoint):
	path=root.split(os.sep)
	p = ""
	for i in path:
		p += i + "/"
	#f.write(p)
	#f.write('\n')
	A[p] =files
	for i in dirs:
		A[p].append(i)

curPath=startPoint+"/"
path = curPath+"> "

while True:

	print(path,end='')
	command=input()
	commandParts = command.split(' ')

	if commandParts[0] == "exit":
		print("Exiting..")
		break;

	elif commandParts[1] == "--help":
		helpCommand(commandParts)

	elif commandParts[0] == 'ls':
		if len(commandParts) == 1:
			printDirectories(A[curPath],'   ')
		elif len(commandParts)==2 and commandParts[1]=='-1':
			printDirectories(A[curPath],'\n')
		elif len(commandParts)==2 and commandParts[1]=='-r':
			printReverseDirectories(A[curPath],'   ')
		elif len(commandParts)==2 and commandParts[1]=='-a':
			printAllDirectories(A[curPath],'   ')
		else :
			#needs to implement for path after switch from root
			if len(commandParts)>2:
			 	lsCommand(startPoint+commandParts[2],A,commandParts[1]) 
			else:
				lsCommand(startPoint+commandParts[1], A,-100)

	elif commandParts[0] == "cd":
		curPath = cdCommand(commandParts[1],curPath, A)
		path = curPath+">"

	elif commandParts[0] == "pwd":
		pwdCommand(curPath)
		
	
