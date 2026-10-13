
school_friends = input("Enter school friends separated by spaces: ").split()
college_friends = input("Enter college friends separated by spaces: ").split()

common_friends = set(school_friends).intersection(set(college_friends))

print("Common friends (Set intersection method):", list(common_friends))
