# PROG 4: To Remove Elements From The List

# Write The Code Here

color_list=['Red', 'Green', 'Pink', 'Blue', 'Black', 'Purple', 'Yellow', 'Magenta', 'Brown']

index_to_remove=[0,2,5]
updated_color=[]

for index, color in enumerate(color_list):
  if index not in index_to_remove:
    updated_color.append(color)
  
print("Original List is :",color_list)
print("Updated LIst is :",updated_color)



