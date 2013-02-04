'''
Documentation, License etc.

@package MemeticSoup
'''

import numpy as np

population = np.random.randint(low=0, high=2, size=(100, 10))
fitnesses = np.zeros(shape=(100, 1), dtype=np.float32)
total_fitness = fitnesses.sum()

MUTATION_RATE = 0.2
CROSSOVER_RATE = 0.75

def pmx(Dad, Mum):
    if np.random.rand() > CROSSOVER_RATE or Dad == Mum:
        return
    
    Baby1 = Dad
    Baby2 = Mum
    
    map_start = np.random.randint(0, len(Mum) - 2)
    map_end   = map_start
    while map_end <= map_start:
        map_end = np.random.randint(0, len(Mum) - 1)
    
    for pos in range(map_start, map_end + 1):
        g1 = Dad[pos]
        g2 = Mum[pos]
        
        if g1 != g2:
            # for Baby1
            pos1 = -1
            pos2 = -1
            for i in range(0, len(Baby1)):
                if Baby1[i] == g1:
                    pos1 = i
                    continue
                
                if Baby1[i] == g2:
                    pos2 = i
            
            tmp_g1 = Baby1[pos1]
            tmp_g2 = Baby1[pos2]
            
            Baby1[pos1] = tmp_g2
            Baby1[pos2] = tmp_g1
            
            # follow the same procedure for Baby2
            pos1 = -1
            pos2 = -1
            for i in range(0, len(Baby2)):
                if Baby2[i] == g1:
                    pos2 = i
                    continue
                
                if Baby2[i] == g2:
                    pos2 = i
            
            tmp_g1 = Baby2[pos1]
            tmp_g2 = Baby2[pos2]
            
            Baby2[pos1] = tmp_g2
            Baby2[pos2] = tmp_g1
    
    return (Baby1, Baby2)

def roulette_wheel(population):
    slice = np.random.rand() * total_fitness
    total = 0
    genome= None
    
    for i in range (0, len(population)):
        curr_genome = population[i]
        curr_fitness= fitnesses[i]
        
        total += curr_fitness
        
        if total > slice:
            genome = curr_genome
            break
    
    return genome

def exchange(genome):
    if np.random.random() <= MUTATION_RATE:
        pos1 = np.random.randint(0, len(genome))
        pos2 = pos1
        
        while pos2 == pos1:
            pos2 = np.random.randint(0, len(genome))
        
        chromo1 = genome[pos1]
        chromo2 = genome[pos2]
        genome[pos1] = chromo2
        genome[pos2] = chromo1

def calculate_fitness(genome):
    f = np.random.random()
    return f

if __name__ == '__main__':
    for i in range(len(population)):
    #for genome, fitness in zip(population, fitnesses):
        fitnesses[i] = calculate_fitness(population[i])


