"""
Template file for ECMM462 coursework

Academic Year: 2022/23
Version: 1
Author: Diego Marmsoler
"""
import sys
import re

#Alice
rightsalice = {}
alicemaxprio = ''
alicemaxcat = []
alicecurrentprio = ''
alicecurrentcat = []

file1 = open('alice.txt', 'r')
lines = file1.readlines()
if (len(lines)!=3):
	raise SystemExit("Wrong file format")

c = re.compile('^([wra]?),([wra]?),([wra]?)$')
result=c.search(lines[0])
if (not result):
	raise SystemExit("Wrong file format")
rightsalice[1]=result.group(1)
rightsalice[2]=result.group(2)
rightsalice[3]=result.group(3)

prio = lines[1].strip().split(":")
if (len(prio)!=2):
	raise SystemExit("Wrong file format")

if (prio[0]=='h' or prio[0]=='l'):
	alicemaxprio=prio[0]
else:
	raise SystemExit("Wrong file format")

cat = prio[1].split(",")
for c in cat:
	if (c == 'A' or c == 'B' or c =='C'):
		alicemaxcat.append(c)

prio = lines[2].strip().split(":")
if (len(prio)!=2):
	raise SystemExit("Wrong file format")

if (prio[0]=='h' or prio[0]=='l'):
	alicecurrentprio=prio[0]
else:
	raise SystemExit("Wrong file format")

cat = prio[1].split(",")
for c in cat:
	if (c == 'A' or c == 'B' or c =='C'):
		alicecurrentcat.append(c)

#Bob
rightsbob = {}
bobmaxprio = ''
bobmaxcat = []
bobcurrentprio = ''
bobcurrentcat = []

file1 = open('bob.txt', 'r')
lines = file1.readlines()
if (len(lines)!=3):
	raise SystemExit("Wrong file format")

c = re.compile('^([wra]?),([wra]?),([wra]?)$')
result=c.search(lines[0])
if (not result):
	raise SystemExit("Wrong file format")
rightsbob[1]=result.group(1)
rightsbob[2]=result.group(2)
rightsbob[3]=result.group(3)

prio = lines[1].strip().split(":")
if (len(prio)!=2):
	raise SystemExit("Wrong file format")

if (prio[0]=='h' or prio[0]=='l'):
	bobmaxprio=prio[0]
else:
	raise SystemExit("Wrong file format")

cat = prio[1].split(",")
for c in cat:
	if (c == 'A' or c == 'B' or c =='C'):
		bobmaxcat.append(c)

prio = lines[2].strip().split(":")
if (len(prio)!=2):
	raise SystemExit("Wrong file format")

if (prio[0]=='h' or prio[0]=='l'):
	bobcurrentprio=prio[0]
else:
	raise SystemExit("Wrong file format")

cat = prio[1].split(",")
for c in cat:
	if (c == 'A' or c == 'B' or c =='C'):
		bobcurrentcat.append(c)

#Charlie
rightscharlie = {}
charliemaxprio = ''
charliemaxcat = []
charliecurrentprio = ''
charliecurrentcat = []

file1 = open('charlie.txt', 'r')
lines = file1.readlines()
if (len(lines)!=3):
	raise SystemExit("Wrong file format")

c = re.compile('^([wra]?),([wra]?),([wra]?)$')
result=c.search(lines[0])
if (not result):
	raise SystemExit("Wrong file format")
rightscharlie[1]=result.group(1)
rightscharlie[2]=result.group(2)
rightscharlie[3]=result.group(3)

prio = lines[1].strip().split(":")
if (len(prio)!=2):
	raise SystemExit("Wrong file format")

if (prio[0]=='h' or prio[0]=='l'):
	charliemaxprio=prio[0]
else:
	raise SystemExit("Wrong file format")

cat = prio[1].split(",")
for c in cat:
	if (c == 'A' or c == 'B' or c =='C'):
		charliemaxcat.append(c)

prio = lines[2].strip().split(":")
if (len(prio)!=2):
	raise SystemExit("Wrong file format")

if (prio[0]=='h' or prio[0]=='l'):
	charliecurrentprio=prio[0]
else:
	raise SystemExit("Wrong file format")

cat = prio[1].split(",")
for c in cat:
	if (c == 'A' or c == 'B' or c =='C'):
		charliecurrentcat.append(c)

def switch_function(o, s, name, function):
    # Loop through the values in the given object
    for value in o:
        # Check the value and return False if the corresponding condition is not satisfied
        if value == '1':
            if 'A' not in s or 'B' not in s: return False
        elif value == '2':
            if 'C' not in s: return False
        elif value == '3':
            if 'B' not in s: return False
    # All conditions are satisfied, return True
    return True

def ssc(alice, bob, charlie):
    # Initialize the data
    circle = [alice, bob, charlie]
    circle_name = ['alice', 'bob', 'charlie']
    
    # Traverse each member in the data
    for i in range(len(circle)):
        obj = circle[i]
        # Check if the current member has a document
        if len(obj):
            # Get the document name and rights
            doc, rights = next(iter(obj)), next(iter(obj.values()))
            # Check if the current member has write or read rights
            if rights == 'w' or rights == 'r':
                # Call the switch_function to check if the rights are valid
                res = switch_function(doc, alicemaxcat if circle_name[i] == 'alice' else bobmaxcat if circle_name[i] == 'bob' else charliemaxcat, circle_name[i], 'ssc')
                if not res: 
                    return False
    # All rights are valid, return True
    return True


def star(alice, bob, charlie):
    # Initialize the data
    circle = [alice, bob, charlie]
    circle_name = ['alice', 'bob', 'charlie']
    
    # Traverse each member in the data
    for i in range(len(circle)):
        obj = circle[i]
        # Check if the current member has a document
        if len(obj):
            # Get the document name and rights
            doc, rights = next(iter(obj)), next(iter(obj.values()))
            # Check if the current member has access, write or read rights
            if rights == 'a' or rights == 'r' or rights == 'w':
                # Call the switch_function to check if the rights are valid
                res = switch_function(doc, alicecurrentcat if circle_name[i] == 'alice' else bobcurrentcat if circle_name[i] == 'bob' else charliecurrentcat, circle_name[i], 'star')
                if not res: 
                    # Return False if the rights are not valid
                    return False
    # All rights are valid, return True
    return True


def ds(alice, bob, charlie):
    # Initialize the data
    circle = [alice, bob, charlie]
    circle_name = ['alice', 'bob', 'charlie']
    # Traverse each member in the data
    for i in range(len(circle)):
        obj = circle[i]
        # Check if the current member has a document
        if len(obj):
            # Get the rights of the current member
            rights = next(iter(obj.values()))
            # Check if the rights of the current member are unique in the circle
            if list((rightsalice if circle_name[i] == 'alice' else rightsbob if circle_name[i] == 'bob' else rightscharlie).values()).count(rights) == 0:
                # Return False if the rights are not unique
                return False
    # All rights are unique, return True
    return True


alice = {}
bob = {}
charlie = {}
c = re.compile('^([ABC]):([123]):([rwa])$')
args=sys.argv[1:]
while (len(args)>0):
	input=args.pop(0)
	result=c.search(input)
	if (not result):
		raise SystemExit("Usage: blpcheck.py [ABC]:[123]:[rwa] ...")
	if (result.group(1)=='A'):
		if result.group(2) in alice:
			raise SystemExit("duplicate entry")
		alice[result.group(2)]=result.group(3)
	if (result.group(1)=='B'):
		if result.group(2) in bob:
			raise SystemExit("duplicate entry")
		bob[result.group(2)]=result.group(3)
	if (result.group(1)=='C'):
		if result.group(2) in charlie:
			raise SystemExit("duplicate entry")
		charlie[result.group(2)]=result.group(3)
print ("SSC: ", "Yes" if ssc(alice, bob, charlie) else "No")
print ("Star: ", "Yes" if star(alice, bob, charlie) else "No")
print ("DS: ", "Yes" if ds(alice, bob, charlie) else "No")

# python3 blpcheck.py A:1:w B:2:r
# SSC : yes
# Star : yes
# DS : no