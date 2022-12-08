"""
Template file for ECMM462 coursework

Academic Year: 2022/23
Version: 1
Author: Diego Marmsoler
"""
import sys
import re

def encrypt(input, rounds, roundkeys):
	# Split the input into left and right halves
	input_l, input_r = [], []
	input_l.append(bin(int(input[0 : (len(input) // 2)], 2)))
	input_r.append(bin(int(input[len(input) // 2 :], 2)))
	
	# Perform the encryption rounds
	index = 1
	while (index < rounds):
		if index == 0: continue
		# Ri = Li-1 ⊕ F(Ri-1， Ki)
		input_l.append(input_r[index - 1])
		input_r.append(bin(int(input_l[index - 1], 2) ^ F(input_r[index - 1], roundkeys[index])))
		index += 1

	# Return the encrypted string
	return ((6 - len(input_l[-1])) * "0" + str(input_l[-1]) + (6 - len(input_r[-1])) * "0" + str(input_r[-1])).replace("0b", "")

def encrypt(input, rounds, roundkeys):
	# Split the input into left and right halves
	input_l, input_r = [], []
	input_l.append(bin(int(input[0 : (len(input) // 2)], 2))) # Get the left half of the input and convert to binary
	input_r.append(bin(int(input[len(input) // 2 :], 2))) # Get the right half of the input and convert to binary

	# Perform the encryption rounds
	index = 1
	while (index < rounds):
		if index == 0: continue  # Skip the first round, as the input has already been split into left and right halves
		# set Ri = Li-1 ⊕ F(Ri-1， Ki)
		# The current left half is the previous right half
		input_l.append(input_r[index - 1])  
		# The current right half is the previous left half XORed with the result of the F function
		input_r.append(bin(int(input_l[index - 1], 2) ^ F(input_r[index - 1], roundkeys[index])))  
		index += 1

	# Return the encrypted string
	return ((6 - len(input_l[-1])) * "0" + str(input_l[-1]) + (6 - len(input_r[-1])) * "0" + str(input_r[-1])).replace("0b", "")  # Concatenate the left and right halves and pad with zeros if necessary, then remove the "0b" prefix.

def decrypt(input, rounds, roundkeys):
    # Split the input into left and right halves
    input_l = bin(int(input[0 : (len(input) // 2)], 2))
    input_r = bin(int(input[len(input) // 2 :], 2))

    # Perform "rounds" rounds of decryption
    for i in range(rounds - 1, 0, -1):
        # Set Li = Ri and Ri = Li XOR F(Ri, Ki)
        input_l, input_r = input_r, bin(int(input_l, 2) ^ F(input_r, roundkeys[i]))

    # Return the decrypted output
    return (6 - len(input_l)) * "0" + str(input_l) + (6 - len(input_r)) * "0" + str(input_r)

def F(input, key): # F method, just (A & B) + 1
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