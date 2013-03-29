
import random
from evolutionary_candidate import candidate

def fitFunction(candidate): #define whatever fitness function you want, I just tried a simple one here
    fitness=0
    for x in candidate.bin_rep:
        if x=='1':
            fitness+=1
    return fitness

def generateCandidate(bitlength):

    binrep=''
    for x in range(bitlength): 
        binrep+= str(random.randint(0,1))
    return binrep

def generatePop(popSize, bitlength):

    population=[]
    for i in range(popSize):
        binrep= generateCandidate(bitlength)
        population.append(candidate(binrep))
        
    return population

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
        newGeneration=[]

        for cand in population: #for every candidate, mate then mutate

            if(random.random()<crossProb):
                
                offspring= cand.mate_crossover(population[maxIndex]) #mate with best candidate, producing offspring
                newGeneration.append(offspring) #add this offspring to new generation
            else:
                x=generateCandidate(bitlength) #if mating fails, generate random offspring
                newGeneration.append(candidate(x))
            
        for offspring in newGeneration: #go through everyone in new generation and possibly mutate
            if(random.random()<mutateProb):
                offspring.mutate_switch()

        print "In generation: ", genNum, " - the max fitness was: ", maxFitness
        print "The max fitness candidate was: ", population[maxIndex]
        print "The average fitness of the population was: ", averageFit

        population= newGeneration[:] #update generation
