from dataclasses import dataclass,field

@dataclass
class Student:
    id:int=field(repr=False) # id print ni hogi
    name:str
    clg:str=field(default="Chitkara")

s1=Student(1051,"AKSHAY","CU")
print(s1)


# showing that all object share memory.
@dataclass
class Shared:
    vehicle=[]

    def add_vehicle(self,item):
        self.vehicle.append(item)

S1=Shared()
S1.add_vehicle("Audi")

S2=Shared()
print(S2.vehicle)

# solution is use default_factory

@dataclass
class Hub:
    vehicle:list=field(default_factory=list)

    def add_vehicle(self,item):
            self.vehicle.append(item)

H1=Hub()
H1.add_vehicle("BMW")
H2=Hub()
print(H2.vehicle)  # problem solved

# automatically provide init, eq, repr.
# repr is very good feauture.

# important methods under dataclass are

# 1. feild(default=) - user argument good if not provide default.else
# 2. feild(repr=False) -> you cannot print this variable
# 3. feild(compare=Flase) -> cannot compare
# 4. feild(init-False) -> constructor me nhi ayega
# 5. default_factory=list -> sarre objects ka apna memory eg list
# 6. post_init -> used for validation
# 7. frozen=True -> ek baar class ke object ki attributes initiate kar diye phir vh change ni ho sakte.
# 
# 
# amzing feauture i like is :
# 1. no constructor 
# 2, post init
# 3. repr to print
# 4. default_factory - no shared memory 
# 5. frozen set - no object attribute change


