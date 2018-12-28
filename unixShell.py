import os

def printDirectories(dirsAndFiles):
	if len(dirsAndFiles) == 0:
		print(end='')
	else:
		for i in dirsAndFiles:
			print(i, end='   ')
		print()

def goBehind(cmd):
	count=1
	for i in reversed(cmd[:-1]):
		if i == "/":
			break;
		count=count+1
	return cmd[:-count]

def lsCommand(cmd, A):
	if cmd[len(cmd)-1] != "/":
		cmd+='/'
	A[cmd].sort()
	printDirectories(A[cmd])

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
		

def catCommand(cmd, A):
	print('Hello')


#f = open("tree1.txt","w")
A = {}
startPoint = '/'
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

	if commandParts[0] == 'ls':
		if len(commandParts) == 1:
			printDirectories(A[curPath])
		else : 
			lsCommand(startPoint+commandParts[1], A)

	elif commandParts[0] == "cat":
		catCommand(commandParts)

	elif commandParts[0] == "cd":
		curPath = cdCommand(commandParts[1],curPath, A)
		path = curPath+">"

	elif commandParts[0] == "pwd":
		pwdCommand(curPath)
		
	
