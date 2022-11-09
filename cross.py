import random
import re

#with open("BankProblem.txt") as file_pi
    #data = file_pi.read()

population = {}
dict = {}
p = 10
tol_value =  285 
f = open("BankProblem.txt", 'r')
data = f.readlines()

i = 0
while i < len(data):
    if (data[i].find("bag") == 1):
        dict[int(re.findall("\d+", data[i])[0], 10) - 1] = [float(re.findall(r"[-+]?\d*\.\d+|\d+", data[i+1])[0]), float(re.findall(r"[-+]?\d*\.\d+|\d+", data[i+2])[0])]
    i += 1  
    ## convert txt to dict with float

for times in range(p): ## inital
    temp, sum = [], 0 ## sum为当前背包重量 temp为当前队列
    while (True):
        now_key = random.randint(0, 99)
        if (now_key not in temp):
            temp.append(now_key)
            sum += dict[now_key][0]
            if (sum > tol_value):
                temp.pop()
                sum -= dict[now_key][0]
                break
        # print(f'总和为{sum} 选取{now_key}bag 增加{dict[now_key][0]}')
    population[times] = temp
print(population)

def fitness(array_num):
    sum_fit, sum_weight = 0, 0
    sum_value = 0
    # print(array_num)
    for i in array_num:
        sum_fit += dict[i][1] / dict[i][0]
        sum_weight += dict[i][0]
        sum_value += dict[i][1]
    # print(sum_weight, sum_weight)
    # sum_ = [sum_ += dict[j][0] for i in array for j in population[i]]
    if sum_weight < 285 :
        return sum_fit
    else:
        print(f'{sum_weight} too heavy, jump it')
        return -1

gernation, times = 10000, 0
lowest_index = 0
lowest_fitness = fitness(population[lowest_index])
for i in population:
    if (fitness(population[i]) < lowest_fitness):
        lowest_fitness = fitness(population[i])
        lowest_index = i
print(lowest_fitness, lowest_index)

import sys
sys.setrecursionlimit(11000)

def mutation():
    # binary tournament
    # a = [random.randint(0, p - 1) for _ in range(2)]
    
    global times, lowest_index, lowest_fitness
    
    # parents = [random.randint(0, p - 1) for _ in range(2)]
    # print(population)
    while (True):
        i = random.randint(0, len(population) - 1)
        j = random.randint(0, len(population) - 1)
        if i != j:
            break
        
    p1, p2 = population[i], population[j]
    index = random.randint(0, len(p1) if len(p1) < len(p2) else len(p2))
    
    print(f'round {times + 1}')
    # print(parents, index, len(p1), len(p2))
    
    e = p1[0 : index] + p2[index : len(p2)]
    f = p2[0 : index] + p1[index: len(p1)]
    
    # mutation 1 times TODO: mulity mutation
    while (True): 
        a, b = random.randint(0, 99), random.randint(0, 99)
        if (a != b and a not in p1 and b not in p2):
            e[random.randint(0, len(e)) - 1] = a
            f[random.randint(0, len(f)) - 1] = b
            break
    
    if (fitness(e) > fitness(f)):
        child = e
    else:
        child = f

    if (fitness(child) > fitness(population[lowest_index])):
        population[lowest_index] = child
        print(f'mutation successfully number {lowest_index} changed')
        lowest_fitness = fitness(child)
        
        for i in population:
            if (fitness(population[i]) < fitness(population[lowest_index])):
                lowest_index = i
                lowest_fitness = fitness(population[i])

            
    times += 1
    if (times < gernation): mutation()

mutation()

print(population)

index, sum_value = 0, 0

for i in population:
    sum = 0
    for j in population[i]:
        sum += j
    
    print(i, "value is", sum, fitness(population[i]))
    if (sum > sum_value):
        index = i
        sum_value = sum

print("max", index, sum_value)



