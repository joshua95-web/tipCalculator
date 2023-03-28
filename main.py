print("welcome to TIPCALCULATOR\n")

billTotal = input("What is the total bill?\n")
billTotalInt = int(billTotal)

tipPercentage = input("What percentage would you like to tip? 10, 12 or 15?\n")
tipPercentageInt = int(tipPercentage)

numberOfPeople = input("Split the bill between how many people?\n")
numberOfPeopleInt = int(numberOfPeople)

billSplit = billTotalInt / numberOfPeopleInt
#billSplitInt = int(billSplit)

eachTip = (tipPercentageInt / 100) * billSplit

eachPays = billSplit + eachTip

eachPaysRounded = round(eachPays, 2)

eachPaysString = str(eachPaysRounded)

print("Each person should pay " + eachPaysString)