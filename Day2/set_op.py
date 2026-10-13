
school_friends = input("Enter school friends separated by spaces: ").split()
college_friends = input("Enter college friends separated by spaces: ").split()

common_friends = set(school_friends) & set(college_friends)

print("Common friends (Set & operator):", list(common_friends))
