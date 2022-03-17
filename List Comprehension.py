def doubleExample():
    list1 = [2, 3]
    doubled = [num*2 for num in list1]
    print(doubled)
doubleExample()

def startsWithExample():
    friends = ["Rolf", "Sally", "Sam"]
    starts_with_S = [friend  for friend in friends  if friend.startswith("S")]
    print(starts_with_S)
startsWithExample()