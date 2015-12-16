import sys


#FUNCTIONS


#Display function takes in an input, its length, and a flag indicating
#Whether the input is a string or integer
def display(Z,n,flag):
	if(flag == "int"):
		for i in range(n):
			print Z[i],
		print
		exit()
	if(flag == "str"):
		for i in range(n):
			sys.stdout.write(Z[i])
		print

#maxLyn function takes in a string, its length, and an index
def maxLyn(Z,n,k):
	#if last character, return 1
	if(k==n-1):
		return 1
	p=1
	#loop through the characters from k+1 to n
	for i in range(k+1,n,1):
		if(Z[i-p] != Z[i]):
			if(Z[i-p] > Z[i]):
				return p
			else:
				p=i+1-k
	return p


#MAIN


#Gets input string and stores that string in x
x = raw_input("Enter your string: ")

#Checks if the length of the string is less than 1 or
#greater than 20
if(len(x) <1 or len(x) > 20):
	print "String lenth error"
	exit()

#Checks if all characters in x are lowercase characters
for i in x:
	if i.islower():
		continue
	else:
		print "String format error"
		exit()


n = len(x)
k = 0
index = 0
a = []

#Calling the display function to check
#the word that was just entered
display(x,n,"str")

#looping through the input string
for i in x:
	#Calling maxLyn for each loop thorugh
	a.append(maxLyn(x,n,index))
	index+=1

#displaying the final output integer
display(a,n,"int")
