print("We'll catagorise the expensenes into 2 main types, expenses for all and some ppl")
while True:
    numberOfPeople = input("How many of us here? Ans: ")
    try:
        checkingVariable = int(numberOfPeople)
        break
    except:
        print("Number of ppl can only be integers!..now try again please")
listName = []
listOfNames = []


def expenses(list, cost_value):
    def payerSubtraction(list2, costSub, list4):
        while True:
            paidByWho = input("Who paid it? Ans: ")
            usefulCost = -costSub
            if not paidByWho in list4:
                print("The payer's name doesn't match with any of the names in our group..Try again please..")
            else :
              break
        for z in range(checkingVariable):
                if paidByWho in list2[z]:
                    list2[z].append(usefulCost)
        return list2

    costForAll = float(cost_value) / checkingVariable
    for k in range(checkingVariable):
        list[k].append(costForAll)
    payerSubtraction(list, float(cost_value), listOfNames)
    return list


def expenses2(list3, cost_value2):
    def payerSubtraction(list2, costSub, list4):
        while True:
            paidByWho = input("Who paid it? Ans: ")
            usefulCost = -costSub
            if not paidByWho in list4:
                print("The payer's name doesn't match with any of the names in our group..Try again please..")
            else :
              break
        for z in range(checkingVariable):
                if paidByWho in list2[z]:
                    list2[z].append(usefulCost)
        return list2
    while True:
        howMany = input("How many people are involved in this expense? Ans: ")
        try:
            checkingVariable = int(howMany)
            break
        except:
            print("Number of ppl can only be integers!..now try again please")
    costForSome = float(cost_value2) / int(howMany)
    for q in range(int(howMany)):
        names = input("Who are they? (1 by 1) Ans: ")
        for m in range(checkingVariable):
            testingVariable = names in list3[m]
            if testingVariable:
                list3[m].append(costForSome)
    payerSubtraction(list3, float(cost_value2), listOfNames)
    return list3


# create a big list containing everyone
for i in range(checkingVariable):
    theNames = input("The names (one name at a time) Ans: ")
    listName.append([theNames])
    listOfNames.append(theNames)
# displaying all that has been spent and used
print(
    "From now, please enter the price for each item one by one and type 'Phol is brilliant' for the cost when you are finished with each type.")
print("Here are expenses, paid for all people.")
while True:
    cost = input("How much did it cost (in £)? Ans: ")
    try:
        if cost == "Phol is brilliant":
            break
        else:
            expenses(listName, cost)
    except:
        print("Something ain't right..try again you idiot")

print("Next is for-some regime!")
while True:
    cost2 = input("How much did it cost (in £)? Ans: ")
    try:
        if cost2 == "Phol is brilliant":
            break
        else:
            expenses2(listName, cost2)
    except:
        print("Something ain't right..try again you idiot")


def sumFunction(list3, index):
    ans = list3[index][1]
    for X in range(2, len(list3[index])):
        ans = ans + list3[index][X]
    del list3[index][1:]
    ans2 = int(ans * 1000) / 1000
    list3[index].append(ans2)
    return list3


# finding financial balance for each person
newList = []
anotherRandomList = []
for u in range(checkingVariable):
    sumFunction(listName, u)
    newList.append(listName[u][1])
    anotherRandomList.append(0)  # will be used to terminate the following while loop
listName.sort(key=lambda x: x[1])
print(
    "So here is the total balance for everybody(positive numbers represent gaining->need to pay others back and the reverse is true for negative numbers)")
print(listName)


def transactionFunction(list4, list5):
    J = 0
    K = len(list4) - 1
    while list5 != anotherRandomList:
        initialValue = list4[J][1]
        finalValue = list4[K][1]
        usefulInitialValue = -initialValue  # for convenience
        if initialValue + finalValue > 0:
            print(listName[K][0], "please transfer £", usefulInitialValue, "to", listName[J][0])
            list4[J][1] = list5[J] = 0
            list4[K][1] = list5[K] = finalValue + initialValue
            J = J + 1
        elif initialValue + finalValue < 0:
            print(listName[K][0], "please transfer £", finalValue, "to", listName[J][0])
            list4[K][1] = list5[K] = 0
            list4[J][1] = list5[J] = finalValue + initialValue
            K = K - 1
        else:
            print(listName[K][0], "please transfer £", finalValue, "to", listName[J][0])
            list4[J][1] = list5[J] = 0
            list4[K][1] = list5[K] = 0
            J = J + 1
            K = K - 1
        # print(list4) , you could execute this code if you wanna follow results from  slowly and clearly
        if list4[J][1] * list4[K][1] > -0.0001:
            break


transactionFunction(listName, newList)

