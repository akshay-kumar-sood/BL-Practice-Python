# PROG 4.1: Using Iteration: Manually finding common friends by iterating over two lists.

# Write The Code Here

# using looping ways
def common_friends(school,college):
  common_list=[]
  for friend in school:
    if friend in college:
      common_list.append(friend)
  return common_list


School_Friends=['John', 'Alice', 'Bob', 'David']
College_Friends= ['Alice', 'Charlie', 'David', 'Eve']

print(f"School Friends : {School_Friends}")
print(f"College Friends : {College_Friends}")

# call function
common_friends(School_Friends,College_Friends)
