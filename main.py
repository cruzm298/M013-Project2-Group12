import random

# explore only
def exploreonly():
    mysum = 0
    for i in range(100): # Visit each cafeteria 100 times. Each time, add it's happiness value.
        happinessCAFE1 = random.normalvariate(9, 3)
        happinessCAFE2 = random.normalvariate(7, 5)
        happinessCAFE3 = random.normalvariate(11, 7)
        mysum = mysum + happinessCAFE1 + happinessCAFE2 + happinessCAFE3
    print(mysum)
    
# exploit only
