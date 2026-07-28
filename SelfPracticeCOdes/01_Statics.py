# PROG 1.1: By Using Statistics Module

# Write The Code Here
import statistics

list = [31.2, 31.5, 30.9, 31.3, 31.7, 31.9, 32.2]

# finding mean 
print(f"Mean Temperature (numpy) : {statistics.mean(list):.2f}")

# finding standard deviation
print(f"Standard Deviation : {statistics.stdev(list):.2f}")