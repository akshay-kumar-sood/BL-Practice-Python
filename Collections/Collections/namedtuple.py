from collections import namedtuple

old_tuple=(1051,"Akshay","Chitkara")
print(old_tuple[0])

# isme pata ni chal ra 1051 kya hai . hame tuple ko dekhna padega.

named_tuple=namedtuple(
    "named_tuple",
    ["id","name","college"]
)

student1=named_tuple(1051,"Akshay","Chitkara")

print(student1.id)
print(student1.name)
print(student1.college)

print(student1._asdict())
print(student1._fields)


print(type(named_tuple))
s="ac"
print(type(s))




# namedtuple class banata hai ek,
# Immutable
# Lightweight
# Memory efficient
# Good for simple dat storage


# use datclass for inheritence for methods 
