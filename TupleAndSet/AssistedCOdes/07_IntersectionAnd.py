# PROG 4.2: Using the & Operator:

# Write The Code Here
def common_friends(school,college):
  res=list(set(school) & set(college))
  print(f"After Union : {res}")


school_Friends=['John', 'Alice', 'Bob', 'David']
College_Friends= ['Alice', 'Charlie', 'David', 'Eve']

print(f"School Friends : {School_Friends}")
print(f"College Friends : {College_Friends}")

# call function
common_friends(School_Friends,College_Friends)
