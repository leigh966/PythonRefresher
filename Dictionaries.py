def allKeys():
    ages = {"Bob": 30, "Steve": 40, "Matt": 20}
    print("All names: ",[key  for key in ages])
allKeys()

def allItems():
    ages = {"Bob": 30, "Steve": 40, "Matt": 20}
    print("All items: ", ages.items()) # List of item tuples
allItems()

def allValues():
    ages = {"Bob": 30, "Steve": 40, "Matt": 20}
    print("All ages: ", ages.values)
allValues()