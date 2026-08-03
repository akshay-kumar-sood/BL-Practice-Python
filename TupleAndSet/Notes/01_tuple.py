# Tuple

# tuple is immutable wheras list is mutable
# heterogenous

import timeit
import sys

# declaration
my_tuple=('hellow',1,2)
print(type(my_tuple))

# access tuple
print(my_tuple[-1])


# tuple vs list
# tuple access time is less
# tuple is memory efficient

# sys module  --> sys.sizeof()
# timeit 

tuple_time=timeit.timeit(stmt=lambda : (1,23,4,5,6,7,8,9,10) , number=10000000)


