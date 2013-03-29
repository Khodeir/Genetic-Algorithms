import random
from evolutionary_candidate import candidate

def generateBinrep(bitlength):
    '''Randomly generate a candidate of given bitlength. Returns a binrep string'''
    binrep=''
    for x in range(bitlength): 
        binrep+= str(random.randint(0,1))
    return binrep

def generatePop(popSize, bitlength):
    '''Create a population of candidates of the given bitlength. Returns a list of candidates'''
    population=[]
    for i in range(popSize):
        binrep= generateBinrep(bitlength)
        population.append(candidate(binrep))
        
    return population

def fitFunction(candidate): #define whatever fitness function you want, I just tried a simple one here
    '''Determines the fitness of a candidate, here based on 1s in binrep. Returns an int or float'''
    fitness=0
    for x in candidate.bin_rep:
        if x=='1':
            fitness+=1
    return fitness

def sampleSpace(population):
    '''Create a sample space where fitter candidates are represented more often than less fit candidates.
        Returns list of candidates(sample space)'''
    sampleSpace=[]
    for cand in population:
        i= cand.fitness
        for x in range(i):
            sampleSpace.append(cand)

    return sampleSpace

def geneticAlgorithm(popSize, bitlength, crossProb, mutateProb, fitFunction, generations):
    '''Executes a GA. First it creates a random population of size popSize, where each candidate's binrep is
       specified by bitlength. Then goes through number of generations, with given evolutionary parameters'''

    population= generatePop(popSize, bitlength) #Generate initial population

    for genNum in range(generations): #each loop is one generation

        maxFitness= 0
        maxIndex= 0
        totalFitness= 0
        for i in range(popSize): #for every candidate evaluate fitness, keep track of fittest
            f= fitFunction(population[i])
            totalFitness+=f
            if f>maxFitness:
                maxFitness=f
                maxIndex=i #note where the maxFitness was found
            population[i].set_fitness(f)
        averageFit= totalFitness/float(popSize)
        
        #at this point, all candidates have an associated fitness, and we know the maxFitness candidate
        for cand in population: #for every candidate normalise fitness into 10 categories
            f=cand.fitness
            f= (f**2)/float(maxFitness**2)
            f*=20
            f=int(f)
            cand.set_fitness(f) #fitness is now a scale of 1 to 20, relative to fittest candidate
            
        matePool= sampleSpace(population)
        newGeneration=[]

        for cand in population: #for every candidate, mate then mutate

            if(random.random()<crossProb):
                i=random.randint(0,len(matePool)-1) #a random index from the mating pool
                mate= matePool[i]
                offspring= cand.mate_crossover(mate) #mating more probable with fit candidates
                newGeneration.append(offspring) #add this offspring to new generation
            else:
                x=generateBinrep(bitlength) #if mating fails, generate random offspring
                newGeneration.append(candidate(x))
            
        for offspring in newGeneration: #go through everyone in new generation and possibly mutate
            if(random.random()<mutateProb):
                offspring.mutate_switch()

        print "In generation: ", genNum, " - the max fitness was: ", maxFitness
        print "The max fitness candidate was: ", population[maxIndex]
        print "The average fitness of the population was: ", averageFit

        population= newGeneration[:] #update generation
