import random

class dip_candidate(object):
    
    def __init__(self, chromosomeA, chromosomeB):
        '''Create an individual candidate with chromosome pairs, binary represented'''
        #should probably introduce some limitations on binrep here (not enough genes == low chance of survival?)
        self.chromosomeA = chromosomeA
        self.chromosomeB = chromosomeB
        self.fitness = -1
        
    def __str__(self):
        return self.chromosomeA + self.chromosomeB

    def __lt__(self, cand):
        return self.fitness<cand.fitness
        
    def set_fitness(self, f):
        self.fitness = f

    def mate_crossover(self, mate):
        '''Return an offspring of self and mate where the genes up to a crossover point come from the first parent,
            then past that point come from the other parent'''
        childbinrep = ''
        maxLength= len(self)
        crossover= random.randint(0,maxLength)
        for i in range(crossover):
            childbinrep += self.bin_rep[i]
        for i in range(maxLength-crossover):
            childbinrep += mate.bin_rep[i]
        offspring= hap_candidate(childbinrep)
        return offspring
        
    def mate_prob(self, mate):
        '''Return an offspring of self and mate where each gene has 50% chance of being from either parent.'''
        childbinrep = ''
        for i in range(len(self.bin_rep)):
            if(random.random()>0.5):
                childbinrep += self.bin_rep[i]
            else:
                childbinrep += mate.bin_rep[i]
        offspring = hap_candidate(childbinrep)
        return offspring

    def mate_sex(self, mate):
        '''Return an offspring of self and mate where exactly (unless odd) half of the genes come from either parent.'''
        childbinrep = ''
        numgenes = len(self.bin_rep)
        selfindicies = random.sample(range(0,numgenes), numgenes//2)
        for i in range(numgenes):
            childbinrep += self.bin_rep[i] if i in selfindicies else mate.bin_rep[i]
        offspring = hap_candidate(childbinrep)
        return offspring
    
    def mutate_switch(self):
        '''Switch a random bit in this candidate's bin_rep.'''
        i = random.randrange(0,len(self.bin_rep))
        e_at_i = '0' if self.bin_rep[i]=='1' else '1'
        self.bin_rep = self.bin_rep[0:i] + e_at_i + self.bin_rep[i+1:]
    
    def mutate_add(self):
        '''Add a random bit to this candidate's bin_rep.'''
        i = random.randrange(0,len(self.bin_rep)+1)
        self.bin_rep = self.bin_rep[0:i] + str(random.randint(0,1)) + self.bin_rep[i:]
