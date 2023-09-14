def payerSubtraction(list2, costSub, listOfNames, checkingVariable):
    """

    This function will be used to append negative value of the cost on the ledger_array(listName) for the payer as they do not owe themself

    """

    while True:
        paidByWho = input("Who paid it? Ans: ")
        usefulCost = -costSub

        if not paidByWho in listOfNames:
            print(
                "The payer's name doesn't match with any of the names in our group..Try again please..")

        else:
            break

    for z in range(checkingVariable):

        if paidByWho in list2[z]:
            list2[z].append(usefulCost)

    return list2


def expenses(listName, cost_value, listOfNames, checkingVariable):
    """

    This function will be used to append a cost for everyone into the ledger_array(listName).

    """

    costForAll = float(cost_value) / checkingVariable

    for k in range(checkingVariable):
        listName[k].append(costForAll)

    payerSubtraction(listName, float(cost_value),
                     listOfNames, checkingVariable)

    return listName


def expenses2(listName, cost_value2, listOfNames, checkingVariable):
    """
    This function was created in order to support the situation where not everyone in the group of people participate in all activities.

    This function will be used to append a cost for those involved in that particular expense into the ledger_array(listName).

    """

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
            testingVariable = names in listName[m]
            if testingVariable:
                listName[m].append(costForSome)

    payerSubtraction(listName, float(cost_value2),
                     listOfNames, checkingVariable)

    return listName


def sumFunction(listName, index):
    """
    This function will sum all the expenses for each individual
    """

    ans = listName[index][1]

    for X in range(2, len(listName[index])):
        ans = ans + listName[index][X]

    del listName[index][1:]

    ans2 = int(ans * 1000) / 1000
    listName[index].append(ans2)

    return listName


def transactionFunction(listName, newList, anotherRandomList):
    """"
    This function will lay out all actions to settle outstanding bills for everyone.
    """

    J = 0  # list index from the start
    K = len(listName) - 1  # list index from the end

    while newList != anotherRandomList:
        initialValue = listName[J][1]
        finalValue = listName[K][1]
        usefulInitialValue = -initialValue  # for convenience

        if initialValue + finalValue > 0:  # The start person still needs to be paid back more
            print(listName[K][0], "please transfer £",
                  usefulInitialValue, "to", listName[J][0])
            listName[J][1] = newList[J] = 0
            listName[K][1] = newList[K] = finalValue + initialValue
            J = J + 1

        elif initialValue + finalValue < 0:  # The end person still needs to pay others back more
            print(listName[K][0], "please transfer £",
                  finalValue, "to", listName[J][0])
            listName[K][1] = newList[K] = 0
            listName[J][1] = newList[J] = finalValue + initialValue
            K = K - 1

        else:
            print(listName[K][0], "please transfer £",
                  finalValue, "to", listName[J][0])
            listName[J][1] = newList[J] = 0
            listName[K][1] = newList[K] = 0
            J = J + 1
            K = K - 1

        if listName[J][1] * listName[K][1] > -0.0001:
            break
