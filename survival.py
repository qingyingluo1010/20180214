#create a class patient and simulate it to death
#variables id and mortality_prob are attributes of class
#when simulate, it is better to provide a max length (yrs)

from enum import Enum
from numpy import np

class healthstat(Enum):
    """health status of patients"""
    ALIVE=1
    DEAD=0

class Patient:
    def __init__(self,id,mortality_prob):
        self._id = id
        self._rnd = np.random
        self._rnd.seed(id)

        self._mortality_prob = mortality_prob
        self._healthstat=healthstat.ALIVE
        self._survivaltime=0 #to check if patient is alive

    def simulate(self,n_time_steps):
        """simulate the patient over the specified simulation length is not reached"""
        t=0 #simulate time
            # while the patient is alive and simulation length is not yet reached
            #project the state to next time state
        while self._healthstat == healthstat.ALIVE and t < n_time_steps:
            # determine if the patient will die during this time-step
            # adding underscore "_" to not allowed to modify attributes in class, they are private class
            if self._rnd.sample() < self._mortality_prob:
                #random number between [0,1]
                self._healthstat = healthstat.DEAD
                self._survivaltime = t+1 #assume deaths occurs at the end of this period
                t+=1
    def get_survival_time(self):
        """returns the patient survival time"""
        if self._helathState==HealthState.DEAD:
            return self._survivaltime
        else:
            return None



class Cohort:
    def __init__(self, id, pop_size, mortality_prob):

        self._patients = [] #list of patients
        self._survivalTimes = [] #list of patient survival times

        #populate the cohort
        for i in range(pop_size):
            #create the patien
            patient = Patient(id*pop_size+i, mortality_prob)
            #add the patient to the cohort
            self._patients.append(patient)
    def simulate(self, n_time_steps):
        # simulate all patients
        for patient in self._patients:
            patient.simulate(n_time_steps)
            #get the survival time
            self._survivalTimes.append(patient.get_survival_time())

    def get_ave_survival_time(self):
        return sum(self._survivalTimes) / len(self._survivalTimes)





