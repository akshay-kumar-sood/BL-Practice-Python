import statistics

numbers=[10,10,10,20,20,20]
mean=statistics.mean(numbers)
median=statistics.median(numbers)

# return first more occuring element
mode=statistics.mode(numbers)

# return a list of multiple mode
multimode=statistics.multimode(numbers)

print(f"means is : {mean}")
print(f"median is : {median}")
print(f"mode is : {mode}")
print(f"multimode is : {multimode}")


