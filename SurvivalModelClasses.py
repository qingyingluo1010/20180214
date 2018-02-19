from enum import Enum
import numpy as np


class HealthStat(Enum):
    """ health status of patients  """
    ALIVE = 1
    DEAD = 0


class Patient(object):
    def __init__(self, id, mortality_prob):
        """ initiates a patient
        :param id: ID of the patient
        :param mortality_prob: probability of death during a time-step (must be in [0,1])
        """
        self._id = id
        self._mortalityProb = mortality_prob
        self._healthState = HealthStat.ALIVE  # assuming all patients are alive at the beginning
        self._survivalTime = 0

    def simulate(self, n_time_steps):
        """ simulate the patient over the specified simulation length """

        t = 0  # simulation current time

        # while the patient is alive and simulation length is not yet reached
        while self._healthState == HealthStat.ALIVE and t < n_time_steps:
            # determine if the patient will die during this time-step
            if np.random.sample() < self._mortalityProb:
                self._healthState = HealthStat.DEAD
                self._survivalTime = t + 1  # assuming deaths occurs at the end of this period

            # increment time
            t += 1

    def get_survival_time(self):
        """ returns the patient survival time """
        return self._survivalTime
