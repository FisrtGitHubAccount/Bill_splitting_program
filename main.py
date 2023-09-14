from all_functions import payerSubtraction, expenses, expenses2, sumFunction, transactionFunction


print("We'll catagorise the expensenes into 2 main types, expenses for all and some ppl")

while True:
    numberOfPeople = input("How many of us here? Ans: ")
    # To show everything on VS code output
    print("How many of us here? Ans: " + numberOfPeople)
    try:
        checkingVariable = int(numberOfPeople)
        break
    except:
        print("Number of ppl can only be integers!..now try again please")

listName = []  # ledger_array containing all the expenses for everyone
listOfNames = []  # for name checking convenience in payerSubtraction() function

# create a big list containing everyone
for i in range(checkingVariable):

    theNames = input("The names (one name at a time) Ans: ")
    # To show everything on VS code output
    print("The names (one name at a time) Ans: " + theNames)

    listName.append([theNames])
    listOfNames.append(theNames)

# displaying all that has been spent and used

print(
    "From now, please enter the price for each item one by one and type 'Phol is brilliant' for the cost when you are finished with each type.")

print("Here are expenses, paid for all people.")

while True:

    cost = input("How much did it cost (in £)? Ans: ")
    # To show everything on VS code output
    print("How much did it cost (in £)? Ans: " + cost)

    try:
        if cost == "Phol is brilliant":
            break
        else:
            expenses(listName, cost, listOfNames, checkingVariable)

    except:
        print("Something ain't right..try again")

print("Next is for-some regime!")

while True:
    cost2 = input("How much did it cost (in £)? Ans: ")
    # To show everything on VS code output
    print("How much did it cost (in £)? Ans: " + cost)

    try:
        if cost2 == "Phol is brilliant":
            break
        else:
            expenses2(listName, cost2, listOfNames, checkingVariable)
    except:
        print("Something ain't right..try again")


# finding financial balance for each person

newList = []        # newList will record the total individual expense for each person
anotherRandomList = []  # will be used to terminate the following while loop

for u in range(checkingVariable):

    sumFunction(listName, u)
    newList.append(listName[u][1])
    anotherRandomList.append(0)

# sort the ledger_array according to their total outstanding balance
listName.sort(key=lambda x: x[1])

print(
    "So here is the total balance for everybody(positive numbers represent gaining->need to pay others back and the reverse is true for negative numbers)")

print(listName)


transactionFunction(listName, newList, anotherRandomList)
