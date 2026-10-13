
school_friends = input("Enter school friends separated by spaces: ").split()
college_friends = input("Enter college friends separated by spaces: ").split()

common_friends = []

for friend in school_friends:
    if friend in college_friends:
        common_friends.append(friend)

print("Common friends (Iterative method):", common_friends)
