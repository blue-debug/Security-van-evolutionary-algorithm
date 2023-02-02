import random
import re
import matplotlib.pyplot as plt

#with open("BankProblem.txt") as file_pi
    #data = file_pi.read()

population = {}
dict = {}
p = 10
tol_weight =  285
gernation = 10000
mutation_times = 1

f = open("BankProblem.txt", 'r')
data = f.readlines()

i = 0
while i < len(data):
    if (data[i].find("bag") == 1):
        dict[int(re.findall("\d+", data[i])[0], 10) - 1] = [float(re.findall(r"[-+]?\d*\.\d+|\d+", data[i+1])[0]), float(re.findall(r"[-+]?\d*\.\d+|\d+", data[i+2])[0])]
    i += 1  
    ## use regular exgression to  convert txt to dict with float

for times in range(p): ## inital
    temp, sum = [], 0
    while (True):
        now_key = random.randint(0, 99)
        if (now_key not in temp):
            temp.append(now_key)
            sum += dict[now_key][0]
            if (sum > tol_weight): ## add items until weight more than 285
                temp.pop()
                sum -= dict[now_key][0]
                break  
    population[times] = temp
print(population)

def crossover(parent_l, parent_r):
    # single point crossover
    # e = p1[0 : index] + p2[index : len(p2)]
    # f = p2[0 : index] + p1[index : len(p1)]
    # res = parent_l[0 : index] + parent_r[index : len(parent_r)]

    # random single point crossover
    index = random.randint(1, len(parent_l) - 1 if len(parent_l) < len(parent_r) else len(parent_r) - 1)
    res = parent_l[0 : index] if random.randint(0, 1) else parent_l[index : len(parent_l)] + parent_r[0 : index] if random.randint(0, 1) else parent_r[index : len(parent_r)]

    for i in res:
        count = 0
        for j in res:
            if (i == j):
                count += 1
        if count >= 2:
            return [1, 1, 1, 1]     ## assigned res to make this evolution false if find repeated bag
    return res 

def mutation(kid, times):
    for _ in range(times):
        while(True):
            mutation_index = random.randint(0, 99)
            if (mutation_index not in kid):
                kid[random.randint(0, len(kid)) - 1] = mutation_index ## random choose index have a successful muatation if original list dosen't have it
                break
    return kid

def fitness(array_num):
    sum_fit, sum_weight, sum_value = 0, 0, 0

    for i in array_num:
        sum_fit += dict[i][1] / dict[i][0]
        sum_weight += dict[i][0]
        sum_value += dict[i][1]
    # sum_ = [sum_ += dict[j][0] for i in array for j in population[i]]
    if sum_weight < 285 :
        return sum_fit * sum_value ## fitness fuc is value * value / weight
    else:
        print(f'{sum_weight} too heavy, jump it')
        return -1

def binary_tournament():
    while (True):
        i = random.randint(0, len(population) - 1)
        j = random.randint(0, len(population) - 1) 
        if i != j: break
    return i if fitness(population[i]) > fitness(population[j]) else j ## random choose the best parent into two players

import sys
sys.setrecursionlimit(11000)

round = 0
lowest_index = 0
lowest_fitness = fitness(population[lowest_index])
for i in population:
    if (fitness(population[i]) < lowest_fitness):
        lowest_fitness = fitness(population[i])
        lowest_index = i
        
print(lowest_fitness, lowest_index)

average_fitness = []

def main():
    global round, lowest_index, lowest_fitness
    # a = [random.randint(0, p - 1) for _ in range(2)]
    # parents = [random.randint(0, p - 1) for _ in range(2)]

    p1 = population[binary_tournament()]
    p2 = population[binary_tournament()]
    
    print(f'round {round + 1}')

    e = crossover(p1, p2)
    f = crossover(p1, p2)

    e = mutation(e, mutation_times)
    f = mutation(f, mutation_times)
    
    if (fitness(e) > fitness(f)):
        child = e
    else:
        child = f

    if (fitness(child) > fitness(population[lowest_index])):
        population[lowest_index] = child
        lowest_fitness = fitness(child)
        print(f'pop {lowest_index} will be changed')
        
        for i in population:
            if (fitness(population[i]) < fitness(population[lowest_index])):
                lowest_index = i
                lowest_fitness = fitness(population[i])

    max_value = 0
    for i in population:
        sum = 0
        sum_weight = 0
        for j in population[i]:
            sum += dict[j][1]
            sum_weight += dict[j][0]
        
        if (sum > max_value):
            max_value = sum
    
    average_fitness.append(max_value)

    round += 1
    if (round < gernation): main()

main()

print(population)

index, max_value, max_weight = 0, 0, 0

for i in population:
    sum = 0
    sum_weight = 0
    for j in population[i]:
        sum += dict[j][1]
        sum_weight += dict[j][0]
    
    print(i, "value is", sum, "weight is", sum_weight, "fitness is",  fitness(population[i]))
    if (sum > max_value):
        index = i
        max_value = sum
        max_weight = sum_weight

print(f'best {max_value} {max_weight} {p} {mutation_times}')

x = range(len(average_fitness))
plt.plot(x, average_fitness)


# test cmd
# for i in `seq 1 10`; do python3 cross.py | grep best; done 


