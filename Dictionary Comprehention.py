def keyByNameOfTuple():
    users = [
        (0, "Bob", "password123"),
        (1, "Rob", "password456"),
        (2, "Rolf", "password789"),
        (3, "Prof", "password9000")
    ]

    username_mapping = {user[1]: user  for user in users}
    print("All users: ", username_mapping)
    print("Rob's info: ", username_mapping["Rob"])

keyByNameOfTuple()