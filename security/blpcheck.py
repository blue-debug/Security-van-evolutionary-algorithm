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
def domfunction(o, s, name, function):
    # print(o,s,name,function)
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
                return False
        elif value == '2':
            docv = 'C'
            if docv in s:
                print(name,'',function,' is pass')
            else :
                print(name,'',function,' is failed')
                return False
        elif value == '3':
            docv = 'B'
            if docv in s:
                print(name,'',function,' is pass')
            else :
                print(name,'',function,' is failed')
                return False
    
def ssc(alice, bob, charlie):
    circle = [alice, bob, charlie]
    circle_name = ['alice', 'bob', 'charlie']
    # circle = [{'alice', alice}, {'bob', bob}, {'charlice',charlie}]
    for i in range(len(circle)):
        obj = circle[i]
        print(i, obj)
        if len(obj):
            print(f'{obj} key {next(iter(obj))} value, {next(iter(obj.values()))}')
            doc = next(iter(obj))
            rights = next(iter(obj.values()))
            if rights == 'w' or rights == 'r':
                print(f'{circle_name[i]} ssc check is starting')
                res = domfunction(doc, alicemaxcat if circle_name[i] == 'alice' else bobmaxcat if circle_name[i] == 'bob' else charliemaxcat, circle_name[i], 'ssc')
                if not res: 
                    print('fail')
                    return True
    return False

def star(alice, bob, charlie):
    circle = [alice, bob, charlie]
    circle_name = ['alice', 'bob', 'charlie']
    for i in range(len(circle)):
        obj = circle[i]
        if len(obj):
            doc = next(iter(obj))
            rights = next(iter(obj.values()))
            if rights == 'a' or rights == 'r' or rights == 'w':
                res = domfunction(doc, alicecurrentcat if circle_name[i] == 'alice' else bobcurrentcat if circle_name[i] == 'bob' else charliecurrentcat, circle_name[i], 'star')
                if not res: return True
    return False

def ds(alice, bob, charlie):
    circle = [alice, bob, charlie]
    circle_name = ['alice', 'bob', 'charlie']
    for i in range(len(circle)):
        obj = circle[i]
        if len(obj):
            rights = next(iter(obj.values()))
            if list((rightsalice if circle_name[i] == 'alice' else rightsbob if circle_name[i] == 'bob' else rightscharlie).values()).count(rights) > 0:
                print(f'{circle_name[i]} ds check passed')
    return True

    # if len(alice) !=0:	 
    #     alice_rights = next(iter(alice.values()))
    #     print(rightsalice, "alice", alice_rights)
    #     if list(rightsalice.values()).count(alice_rights) > 0:
    #         print('Alice ds check is pass')
    # if len(bob) !=0:	 
    #     bob_rights = next(iter(bob.values()))
    #     if list(rightsbob).count(bob_rights) > 0:
    #         print('Bob ds check is pass')
    # if len(charlie) !=0:	 
    #     charlis_rights = next(iter(charlie.values()))
    #     if list(rightscharlie).count(charlis_rights) > 0:
    #         print('charlie ds check is pass')

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