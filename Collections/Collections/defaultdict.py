from collections import defaultdict

vehicle_map=defaultdict(list)
vehicle_map["ELectricCar"].add("Tesla")
print(vehicle_map)



# summary
# it solves a big problem of traditional dictionary. 
# we cannot direct insert key and value directly we have to insert a empty list then on that key we have to append values.
# but in defaultdict we simply do dict["Car"].append("tesla")
# we can pass list,tuple,set,string,int any callable.
# if it found nothing it use the  callable we have passed to it.



