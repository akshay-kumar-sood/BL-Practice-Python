# used to maintain the order in dictionary 

from collections import OrderedDict

student=OrderedDict()

student["A"]=10
student["B"]=20
student["C"]=30

print(student)

teacher=OrderedDict()

teacher["A"]=10
teacher["B"]=20
teacher["C"]=30

# move to end
teacher.move_to_end("A")

topper={}
topper["A"]=10
topper["B"]=20
topper["C"]=30
print(topper)


loser={}
loser["B"]=20
loser["A"]=10
loser["C"]=30

print(loser==student)
print(teacher==student)


# Summary
# before python 3.7 dictionary do not store values in order. BUt later on it started storing in order.
# so ordereddict primary purpose is gone.
# still relevant because
# 1. == operation 
# noraml dict me order mismatch ho toh vh usse be same manta hai 
# dict1 me pehle key A,B,C hai  dict2 me A,C,B  toh yh true karega return
# ordereddict me yh case ko false karega