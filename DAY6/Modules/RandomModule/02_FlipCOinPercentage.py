# PROG 1.1: To Implement Single Function

# Write The Code Here
# PROG 1.1: To Implement Single Function

# Write The Code Here
import random

times=int(input("Enter the number of times to flip the coin : "))
choice_list=["H","T"]



def no_of_head(times) ->int:
    cnt=0
    for i in range(times):
        str=random.choice(choice_list)
        #print(str)
        if(str=='H'):
            cnt+=1
        
    return cnt

prob=no_of_head(times)
#print("prob",prob)
#print("times",times)
percentage=(prob/times) * 100
#print("percentage",percentage)
print(f"After flipping the coin {times} time, the percentage of times head has come is : {percentage:.0f} %")