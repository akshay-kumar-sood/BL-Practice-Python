# Prog 1 : Assisted COde

# PROG 1: To Use Join

# Write The Code Here
def word_uppercase():
  place_list=[]

  for i in range(5):
    place=input(f"ENter the name of place {i}: ")
    place_list.append(place)

  print(f"Places stored in list : {place_list}")

  places_str=', '.join(place_list)
  print(places_str.upper())


word_uppercase()


# join syntax

# seperator . join (str)
# convert list to str using seperator