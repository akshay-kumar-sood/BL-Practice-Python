# PROG 5.1: Using the | Operator

# Write The Code Here
School_Friends= ['John', 'Alice', 'Bob', 'David']
College_Friends= ['Alice', 'Charlie', 'David', 'Eve']

print(f"School Friends : {School_Friends}")
print(f"College Friends : {College_Friends}")

res=list(set(School_Friends) | set(College_Friends))
print(f"All Friend (Set | operator) : {res}")