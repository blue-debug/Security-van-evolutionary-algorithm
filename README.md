# Security-van-evolutionary-algorithm

The evolutionary algorithm should be implemented as follows: 
1. Generate an initial population of p randomly generated solutions (where p is a reasonable 
population size discussed in lectures and in the module reading), and evaluate the fitness of 
everything in the population. 
2. Use the binary tournament selection twice (with replacement) to select two parents a and b. 
3. Run crossover on these parents to give 2 children, c and d. 
4. Run mutation on c and d to give two new solutions e and f. Evaluate the fitness of e and f. 
5. Run weakest replacement, first using e, then f. 
6. If a termination criterion has been reached, then stop. Otherwise return to step 2. 
Termination Criterion: Will simply be having reached a maximum number of fitness evaluations which 
is 10,000 (see Implementation and Experimentation below) 
Binary Tournament Selection: Randomly choose a chromosome from the population; call it a. Randomly 
choose another chromosome from the population; call this b. The fittest of these two (breaking ties 
randomly) becomes the selected parent. 
Single-Point Crossover: Randomly select a ‘crossover point’ which should be smaller than the total 
length of the chromosome. Take the two parents and swap the gene values between them ONLY for 
those genes which appear AFTER the crossover point to create two new children.
Mutation: This is dependent on your representation, look at the lecture slides for some ideas on which 
mutation to implement given your representation. Your mutation function must take a single integer 
parameter which will determine how many times it is repeated on a solution (e.g., M(1) – one 
mutation per chromosome, M(3) – 3 mutations). 
Weakest Replacement: If the new solution is fitter than the worst in the population, then overwrite the 
worst (breaking ties randomly) with the new solution. 
Implementation and Experimentation 
Implement the described EA in such a way that you can address the above problem and then run the 
experiments described below and answer the subsequent questions. Note that, in all of the below, a 
single trial means that you run the algorithm once and stop it when 10,000 fitness evaluations have 
been reached. Different trials of the same algorithm should be seeded with different random number 
seeds. 
You should devise your own set of experiments to determine what effect (if any) the following 
parameters have on the performance of the optimisation: 
1. Tournament size(t)
2. Population size (p)
3. Mutation rate (i.e. the parameter identified in the mutation operator above) (m)
Your experiments should assess the performance of the algorithm over a number of randomly seeded 
trials for each setting of t, p, m, to provide robust results