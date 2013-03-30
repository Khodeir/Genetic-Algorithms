import random
from evolutionary_candidate import candidate

def fitFunction(candidate):
    '''Determines the fitness of a candidate, here based on 1s in binrep. Returns an int or float'''
    fitness=0
    for x in candidate.bin_rep:
        if x=='1':
            fitness+=1
    return fitness

def fitByMagnitude(candidate):
    return int(candidate.bin_rep ,2)

def generateBinrep(bitlength):
    '''Randomly generate a candidate of given bitlength. Returns a binrep string'''
    binrep=''
    for x in range(bitlength): 
        binrep+= str(random.randint(0,1))
    return binrep

def steepAscent(length, iterations, fitFunction):
    '''Finds optimal solution by steepest ascent method. Uses only one candidate, mutates it every iteration. If mutated
        version is better, make that your new solution'''

    x= generateBinrep(length)
    optimal= candidate(x)
    for i in range(iterations):
        
        candCopy= candidate(optimal.bin_rep)
        candCopy.mutate_switch()
        if fitFunction(candCopy)>fitFunction(optimal):
            optimal= candCopy

        if (i+1)%100==0:
            print 'In iteration ', i, ' max fitness= ', fitFunction(optimal)
            print 'Fittest candidate is: ', optimal
