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

def exploitOnly():
    firstCafe = random.normalvariate(9, 3)
    secondCafe = random.normalvariate(7, 5)
    thirdCafe = random.normalvariate(11, 7)
    sum = 0
    x = 0
    if firstCafe > secondCafe and firstCafe > thirdCafe:
        while x < 297:
            sum = sum + random.normalvariate(9, 3)
            x = x + 1
        print(sum + firstCafe + secondCafe + thirdCafe)
        print(x)
    elif secondCafe > firstCafe and secondCafe > thirdCafe:
        while x < 297:
            sum = sum + random.normalvariate(7, 5)
            x = x + 1
        print(sum + firstCafe + secondCafe + thirdCafe)
        print(x)
    elif thirdCafe > firstCafe and thirdCafe > secondCafe:
        while x < 297:
            sum = sum + random.normalvariate(11, 7)
            x = x + 1
        print(sum + firstCafe + secondCafe + thirdCafe)
