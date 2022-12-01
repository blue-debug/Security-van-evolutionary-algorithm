"""
Template file for ECMM462 coursework

Academic Year: 2022/23
Version: 1
Author: Diego Marmsoler
"""
import sys
import re

def encrypt(input, rounds, roundkeys):
	#TODO: Implement encryption of "input" in "rounds" rounds, using round keys "roundkeys"
	# Li = Ri-1
	# Ri = Li-1 ⊕ F(Ri-1， Ki)
	
	input_l, input_r = [], []
	input_l.append(bin(int(input[0 : (len(input) // 2)], 2)))
	input_r.append(bin(int(input[len(input) // 2 :], 2)))
	print(f'round 1 {input_l} {input_r}')

	index = 1
	while (index < rounds):
		if index == 0: continue
		input_l.append(input_r[index - 1])
		# print(bin(int(input_l[i - 1], 2)), F(input_r[i - 1], roundkeys[i]), bin(int(input_l[i - 1], 2) ^ F(input_r[i - 1], roundkeys[i])))
		input_r.append(bin(int(input_l[index - 1], 2) ^ F(input_r[index - 1], roundkeys[index])))
		print(f'round {index + 1} {input_l} {input_r}')
		index += 1
	
	print(input_l[-1], input_r[-1])	
	return ((6 - len(input_l[-1])) * "0" + str(input_l[-1]) + (6 - len(input_r[-1])) * "0" + str(input_r[-1])).replace("0b", "")

def decrypt(input, rounds, roundkeys):
	#TODO: Implement decryption of "input" in "rounds" rounds, using round keys "roundkeys"
	# Ri = Li+1
    # Li = Ri+1 XOR F(Li+1,Ki)
	# https://cloud.tencent.com/developer/article/1847884

	input_l, input_r = [], []
	input_l.append(bin(int(input[0 : (len(input) // 2)], 2)))
	input_r.append(bin(int(input[len(input) // 2 :], 2)))
	print(f'round 1 {input_l} {input_r}')

	index = rounds

	while (index > 0):
		if index == rounds: continue
		input_l.append(input_r[rounds - index])
		# print(bin(int(input_l[i - 1], 2)), F(input_r[i - 1], roundkeys[i]), bin(int(input_l[i - 1], 2) ^ F(input_r[i - 1], roundkeys[i])))
		input_r.append(bin(int(input_l[rounds - index + 1], 2) ^ F(input_r[rounds - index + 1], roundkeys[rounds - index])))
		print(f'round {rounds - index - 1} {input_l} {input_r}')
		index -= 1

	print(input_l[-1], input_r[-1])	
	return ((6 - len(input_l[-1])) * "0" + str(input_l[-1]) + (6 - len(input_r[-1])) * "0" + str(input_r[-1])).replace("0b", "")

def F(input, key):
	return int(input, 2) & int(key, 2) + 1

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

c = re.compile('^[01]{8}$')
try:
	input=args.pop(0)
except IndexError:
	raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")
if not c.search(input):
	raise SystemExit("input is not a valid bit string")

try:
	rounds=int(args.pop(0))
except IndexError:
	raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")
except ValueError:
	raise SystemExit("rounds is not a valid number")

if(len(args)<rounds):
	raise SystemExit("Usage: {sys.argv[0]} [-d] input rounds roundkey1 roundkey2 ...")

roundkeys=args
c = re.compile('^[01]{4}$')
if not all(c.search(elem) for elem in roundkeys):
	raise SystemExit("round key is not a valid bit string")

if "-d" in opts:
	result = decrypt(input,rounds,roundkeys)
else:
	result = encrypt(input,rounds,roundkeys)

print (result)

# python3 feistel.py 10101010 5 0101 1111 1010 0101 0101