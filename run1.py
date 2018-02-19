import SurvivalModelClasses as Cls

MORTALITY_PROB = 0.1
TIME_STEPS = 40

# create a patient
myPatient = Cls.Patient(id=1, mortality_prob=MORTALITY_PROB)

# simulate the patient
myPatient.simulate(TIME_STEPS)

# print the patient survival time
print(myPatient.get_survival_time())



