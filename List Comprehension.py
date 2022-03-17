def doubleExample():
    list1 = [2, 3]
    doubled = [num*2 for num in list1]
    print(list1, " doubled is ", doubled)
doubleExample()

def startsWithExample():
    friends = ["Rolf", "Sally", "Sam"]
    starts_with_S = [friend  for friend in friends  if friend.startswith("S")]
    print("Names in ", friends," starting with 'S': ", starts_with_S)
startsWithExample()