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

#MAIN
def domfunction(o,s,name,function):
    for index,value in enumerate(o):
        if value == '1':
            docv = 'A'
            if docv in s:
                print(name,'',function,' is pass')
            docv = 'B'
            if docv in s:
                print(name,'',function,' is pass')    
            else :
                print(name,'',function,' is failed')
                return 'fail'
        elif value == '2':
            docv = 'C'
            if docv in s:
                print(name,'',function,' is pass')
            else :
                print(name,'',function,' is failed')
                return 'fail'
        elif value == '3':
            docv = 'B'
            if docv in s:
                print(name,'',function,' is pass')
            else :
                print(name,'',function,' is failed')
                return 'fail'
    
    
def ssc(alice, bob, charlie):
    #TODO: Implement check for simple security condition
    if len(alice) !=0:
       alice_docnum = list(alice.keys())[0]
       alice_subjectright = list(alice.values())[0]

       if alice_subjectright == 'w' or alice_subjectright == 'r':
            print('start checking alice')
            result = domfunction(alice_adocnum, alicemaxcat, 'Alice', 'ssc')
            if result == 'fail': return False
    if len(bob) !=0:
       bob_docnum = list(bob.keys())[0]
       bob_subjectright = list(bob.values())[0]

       if bob_subjectright == 'w' or bob_subjectright == 'r':
            print('start checking bob')
            result = domfunction(bob_docnum, bobmaxcat, 'Bob', 'ssc')
            if result == 'fail': return False
    if len(charlie) !=0:
       charlie_docnum = list(charlie.keys())[0]
       charlie_subjectright = list(charlie.values())[0]

       if charlie_subjectright == 'w' or charlie_subjectright == 'r':
            print('start checking charlie')
            result = domfunction(charlie_docnum, charliemaxcat, 'charlie', 'ssc')
            if result == 'fail': return False
    return True


def star(alice, bob, charlie):
    #TODO: Implement check for star property
    if len(alice) != 0:
       alice_docnum = list(alice.keys())[0]
       print(alice_docnum)
       alice_subjectright = list(alice.values())[0]
       if alice_subjectright == 'a':
           result = domfunction(alice_docnum, alicecurrentcat, 'alice', 'star')
           if result == 'fail': return False
       if alice_subjectright == 'r':
           result = domfunction(alice_docnum, alicecurrentcat, 'alice', 'star')
           if result == 'fail': return False
       if alice_subjectright == 'w':
              result = domfunction(adocnum, alicecurrentcat, 'alice', 'star')
              if result == 'fail': return False
    if len(bob) != 0:
        bob_docnum = list(bob.keys())[0]
        bob_subjectright = list(bob.values())[0]
        if bob_subjectright == 'a':
            result = domfunction(bob_docnum, bobcurrentcat, 'bob', 'star')
            if result == 'fail':
                return False
        if bob_subjectright == 'r':
            result = domfunction(bob_docnum, bobcurrentcat, 'bob', 'star')
            if result == 'fail':
                return False
        if bob_subjectright == 'w':
               result = domfunction(bob_docnum, bobcurrentcat, 'bob', 'star')
               if result == 'fail':
                   return False

    if len(charlie) != 0:
        charlie_docnum = list(charlie.keys())[0]
        charlie_subjectright = list(charlie.values())[0]
        if charlie_subjectright == 'a':
            result = domfunction(charlie_docnum, charliecurrentcat, 'charlie', 'star')
            if result == 'fail': return False
        if charlie_subjectright == 'r':
            result = domfunction(charlie_docnum, charliecurrentcat, 'charlie', 'star')
            if result == 'fail': return False
        if charlie_subjectright == 'w':
               result = domfunction(charlie_docnum, charliecurrentcat, 'charlie', 'star')
               if result == 'fail': return False
    return False

def ds(alice, bob, charlie):
#TODO: Implement check for discretionary security condition
    if len(alice) !=0:	 
        alice_subjectright = list(alice.values())[0]
        if list(rightsalice).count(alice_subjectright) > 0:
            print('Alice check successfully')
    if len(bob) !=0:	 
        bob_subjectright = list(bob.values())[0]
        if list(rightsbob).count(bob_subjectright) > 0:
            print('Bob check successfully')
    if len(charlie) !=0:	 
        charlie_subjectright = list(charlie.values())[0]
        if list(rightscharlie).count(charlie_subjectright) > 0:
            print('charlie  check successfully')
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