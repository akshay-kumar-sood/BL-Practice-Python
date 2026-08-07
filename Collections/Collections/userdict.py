from collections import UserDict

class UpperDict(UserDict):

    def __setitem__(self, key, value):
        super().__setitem__(key.upper(), value)


d = UpperDict()

d["name"] = "Akshay"
d["college"] = "Chitkara"

print(d)





# summary
# List is itself a class.It can be inherited and we can apply custum behviour in that.
# but modifying it the actual list class make it complex and need to take care of many builin operation. 
# wrapper class make composition (has a ) behaviour with list class. means wrapper class internally has a list object. 
# instead of directly applying methods on list we can customize the wrapper class. 

# has methods like setitem,getitem,delitem