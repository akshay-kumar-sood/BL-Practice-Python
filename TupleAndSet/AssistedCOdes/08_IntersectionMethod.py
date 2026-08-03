# PROG 4.3: Using the intersection() Method

# Write The Code Here
def intersect_friends(school,college):
  res=list(set(school).intersection(set(college)))
  print(f"After Intersection : {res}")


school_Friends=['John', 'Alice', 'Bob', 'David']
College_Friends= ['Alice', 'Charlie', 'David', 'Eve']

print(f"School Friends : {school_Friends}")
print(f"College Friends : {College_Friends}")

intersect_friends(school_Friends,College_Friends)