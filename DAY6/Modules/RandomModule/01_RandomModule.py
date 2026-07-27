import random 
# Random module in python 


# randint  --> both end are included --> int 
print(random.randint(1,10))

# uniform  --> both end included --> float
print(random.uniform(0,10))

# random --> generate between 0.0 to 1.0 --> float
print(random.random())

# choice --> generate one elemenet from a sequence
colors=["red","yellow","white","black"]
print(random.choice(colors))

# choices() --> generate multiple items form a sequence -> return list
print(random.choices(colors,k=2))

# sample -> return multiple but without repeating
# crazy it means select 3 diff elements 
# if 1 1 2 2 now it may select 1 1 2
# it doesnot means 1 and 2 are only 2 elements how it would selct 3rd element 

numbers=[1,2,1,2]
print(random.sample(numbers,3))

# sample vs choices
#sample pick unique
#whereas choices does not

# suffle --> rearranges a list
bag=[1,2,3,4,5,6,7,8]
random.shuffle(bag)
print(bag)

# seed --> important for testing when we want same ouput 
# it does what to generate a random number python creates a sequesnces of elemets.
# for example it sequence is like 10 20 22 34 54 2
# if we apply seed so basically it starts from a specific state
# seed 10 20 22 34 54 2
# so next time output would be same 

random.seed(10)
print(random.randint(1, 100))



# final summary
# 1. randit --> int
# 2. uniform --> float
# 3. random --> 0.0 -- 0.1
# 4. choice --> one 
# 5. choices --> many
# 6. sample --> unique choice
# 7. seed --> testing same sequence generation 