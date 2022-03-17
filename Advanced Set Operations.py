friends = {"Charlie", "Bob", "Adam"}
abroad = {"Charlie", "Bob"}

local_friends = friends.difference(abroad) # friends - abroad
print("Friends that are not abroad: ", local_friends)