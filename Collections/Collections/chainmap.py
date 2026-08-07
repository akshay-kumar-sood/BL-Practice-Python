# used less 

from collections import ChainMap

student = {
    "name": "Akshay",
    "age": 22
}

college = {
    "name":"Abhay",
    "college": "Chitkara",
    "branch": "CSE"
}

data = ChainMap(student, college)

print(data)
print(data["name"])
print(data["college"])

# summary 
# chainMap is used to view to dict data together. they do not merge two dict. it provided combined view.
# if duplicate key exist. mtlb name dict1 me bhi hai or dict2 me bhi. toh yh pehle jo name mila vh vapish kar dega.
# it checks left to right
