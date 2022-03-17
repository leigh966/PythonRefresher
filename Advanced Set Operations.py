def differenceExample():
    friends = {"Charlie", "Bob", "Adam"}
    abroad_friends = {"Charlie", "Bob"}

    local_friends = friends.difference(abroad_friends) # friends - abroad
    print("Friends that are not abroad: ", local_friends)

def unionExample():
    friends_that_wear_glasses = {"Charlie", "Bob"}
    friends_that_drive = {"Adam", "Bob"}

    all_friends = friends_that_wear_glasses.union(friends_that_drive) 
    # friends_that_wear_glasses + friends_that_drive
    print("All friends: ", all_friends) # Elements are still unique

differenceExample()
unionExample()