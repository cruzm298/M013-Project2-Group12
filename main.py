import random


def exploreOnly():
    mysum = 0
    for i in range(100): # Visit each cafeteria 100 times. Each time, add it's happiness value.
        happinessCAFE1 = random.normalvariate(9, 3)
        happinessCAFE2 = random.normalvariate(7, 5)
        happinessCAFE3 = random.normalvariate(11, 7)
        mysum = mysum + happinessCAFE1 + happinessCAFE2 + happinessCAFE3
    return(mysum)
    

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
        return (sum + firstCafe + secondCafe + thirdCafe)
    elif secondCafe > firstCafe and secondCafe > thirdCafe:
        while x < 297:
            sum = sum + random.normalvariate(7, 5)
            x = x + 1
        return(sum + firstCafe + secondCafe + thirdCafe)
    else:
        while x < 297:
            sum = sum + random.normalvariate(11, 7)
            x = x + 1
        return(sum + firstCafe + secondCafe + thirdCafe)
        
        
        
def eGreedy(e: int):
    mysum = 0
    happinessCAFE1 = random.normalvariate(9, 3)
    happinessCAFE2 = random.normalvariate(7, 5)
    happinessCAFE3 = random.normalvariate(11, 7)
    ALLhappinessforCAFE1 = [happinessCAFE1]  # Will eventually include all 300 happiness values.
    ALLhappinessforCAFE2 = [happinessCAFE2]
    ALLhappinessforCAFE3 = [happinessCAFE3]
    AVERAGEhappinessofCAFE1 = happinessCAFE1
    AVERAGEhappinessofCAFE2 = happinessCAFE2
    AVERAGEhappinessofCAFE3 = happinessCAFE3
    listofcafe = [happinessCAFE1, happinessCAFE2, happinessCAFE3]
    CurrentBestCafeteria = listofcafe.index(max(listofcafe))  # Finds highest cafe happiness
    mysum = mysum + happinessCAFE1 + happinessCAFE2 + happinessCAFE3
    for i in range(297):
        percentoftheday = random.randint(0, 100)
        item0 = random.normalvariate(9, 3)
        item1 = random.normalvariate(7, 5)
        item2 = random.normalvariate(11, 7)
        RandomListOfCafe = [item0, item1,
                            item2]  # This random list will be refreshed daily.
        if percentoftheday < e:  # The random list will be used in this scenario.
            WhichRandomCafeDoIWantToday = random.randint(0, 2)  # Chooses a random cafeteria for today.
            x = RandomListOfCafe[WhichRandomCafeDoIWantToday]
            mysum = mysum + x
            if WhichRandomCafeDoIWantToday == 0:
                ALLhappinessforCAFE1.append(RandomListOfCafe[0])
            elif WhichRandomCafeDoIWantToday == 1:
                ALLhappinessforCAFE2.append(RandomListOfCafe[1])
            else:
                ALLhappinessforCAFE3.append(RandomListOfCafe[2])

        else:
            if CurrentBestCafeteria == 0:
                temp = random.normalvariate(9, 3)
                mysum = mysum + temp
                ALLhappinessforCAFE1.append(temp)
            elif CurrentBestCafeteria == 1:
                temp = random.normalvariate(7, 5)
                mysum = mysum + temp
                ALLhappinessforCAFE2.append(temp)
            else:
                temp = random.normalvariate(11, 7)
                mysum = mysum + temp
                ALLhappinessforCAFE3.append(temp)
        AVERAGEhappinessofCAFE1 = sum(ALLhappinessforCAFE1) / len([ALLhappinessforCAFE1])
        AVERAGEhappinessofCAFE2 = sum(ALLhappinessforCAFE2) / len([ALLhappinessforCAFE2])
        AVERAGEhappinessofCAFE3 = sum(ALLhappinessforCAFE3) / len([ALLhappinessforCAFE3])
        listofcafe = [AVERAGEhappinessofCAFE1, AVERAGEhappinessofCAFE2, AVERAGEhappinessofCAFE3]
        CurrentBestCafeteria = listofcafe.index(max(listofcafe))
    return (mysum)


def Simulation(t: int, e: int):
    numberoftrialsleft = t
    OptimumHappiness = 11 * 300
    totalresultexploreOnly = 0
    totalresultexploitOnly = 0
    totalresulteGreedy = 0
    while numberoftrialsleft > 0:
        exploreOnlyResult = exploreOnly()
        exploitOnlyResult = exploitOnly()
        eGreedyResult = eGreedy(e)
        totalresultexploreOnly = totalresultexploreOnly + exploreOnlyResult
        totalresultexploitOnly = totalresultexploitOnly + exploitOnlyResult
        totalresulteGreedy = totalresulteGreedy + eGreedyResult

        numberoftrialsleft = numberoftrialsleft - 1

    exploreOnlyExpectedTotalHappiness = 100 * 9 + 100 * 7 + 100 * 11
    exploreOnlyAverageTotalHappiness = totalresultexploreOnly / t
    exploreOnlyExpectedRegret = OptimumHappiness - exploreOnlyExpectedTotalHappiness
    exploreOnlyAverageRegret = OptimumHappiness - exploreOnlyAverageTotalHappiness
    print("Optimum Happiness: ", OptimumHappiness, "\n")
    print("Explore Only Values:")
    print("Expected Total Happiness: ", exploreOnlyExpectedTotalHappiness)  # 2700
    print("Average Total Happiness: ", exploreOnlyAverageTotalHappiness)  #
    print("Expected Regret: ", exploreOnlyExpectedRegret)  # 600
    print("Average Regret: ", exploreOnlyAverageRegret, "\n")  #

    exploitOnlyExpectedTotalHappiness = 9 + 7 + 11 + 297 * 11
    exploitOnlyAverageTotalHappiness = totalresultexploitOnly / t
    exploitOnlyExpectedRegret = OptimumHappiness - exploitOnlyExpectedTotalHappiness
    exploitOnlyAverageRegret = OptimumHappiness - exploitOnlyAverageTotalHappiness
    print("Exploit Only Values:")
    print("Expected Total Happiness: ", exploitOnlyExpectedTotalHappiness)
    print("Average Total Happiness: ", exploitOnlyAverageTotalHappiness)
    print("Expected Regret: ", exploitOnlyExpectedRegret)
    print("Average Regret: ", exploitOnlyAverageRegret, "\n")

    eGreedyExpectedTotalHappiness = (11 * (100 - e) * 0.01 * 300) + (11 * e / 3 * .01 * 300) + (
            9 * e / 3 * .01 * 300) + (7 * e / 3 * .01 * 300)
    eGreedyAverageTotalHappiness = totalresulteGreedy / t
    eGreedyExpectedRegret = OptimumHappiness - eGreedyExpectedTotalHappiness
    eGreedyAverageRegret = OptimumHappiness - eGreedyAverageTotalHappiness
    print("e-Greedy Values:")
    print("Expected Total Happiness: ", eGreedyExpectedTotalHappiness)
    print("Average Total Happiness: ", eGreedyAverageTotalHappiness)
    print("Expected Regret: ", eGreedyExpectedRegret)
    print("Average Regret: ", eGreedyAverageRegret)
