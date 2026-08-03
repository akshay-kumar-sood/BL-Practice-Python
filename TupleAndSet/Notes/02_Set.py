s1={1,2,3,4,5}
print(s1)
print(type(s1))

s1.add(6)

print(s1)

s1.add(6)
print(s1)

# add list
s1.update([5,6,7,8,9])
print(s1)

# remove
s1.remove(9)
print(s1)

# discard
s1.discard(1)

print(s1)

# discard vs remove
# remove throw keyerro if that key is not present 
# discard donot throw error

# intersection
s2={1,2,3}
s3={2,3,4}

s4=s2.intersection(s3)
print(s4)

s5=s2.difference(s3)
print(s5)

# check in s2 which is not present in s3

# uncommon part
s6=s2.symmetric_difference(s3)
print(s6)

# differenece --> check from start present but not in second
# symmetric_difference --> uncommon part


s7=s1.union(s2)
print(s7)

# frozen set
# immmutable set
friends=frozenset(["Akshay","Abhay"])
#friends.add("Harshit")
print(friends)


#add vs update
# remove vs discard
# frozen set

# shorthand
# union |
# intersection & 
# differenece -
# symmetric difference ^