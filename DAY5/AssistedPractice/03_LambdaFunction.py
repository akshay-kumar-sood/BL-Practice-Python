# PROG 3: Lambda Function

# Write The Code Here
user_list=[1,2,3,4,5]
print(f"The original list is : {user_list}")

updated_list=list(map(lambda x:x*2,user_list))
print(f"DOubled list is :{updated_list}")




# enumerate 

# benefit of it is we have index and value at a same time.

user_list=[10,20,30,40,50,60,70]

remove_index=[0,2,4]
updated_list=[]

for index,value in enumerate(user_list):
    if index%2==0 in remove_index:
        updated_list.append(value)


print("Original list is : ",user_list )
print("Updated list is : ",updated_list)


# lambda function 

my_list=[10,20,30,40,50]

new_list=list(map(lambda x:x*2,my_list))
print("OLd list is : ",my_list)
print("UPdated list is :",new_list)

num1=10
y=lambda num1:num1*10
print(y(num1))


# take multiple argument also
num2=lambda num1,num3:num1+num3
print(num2(10,20))


# lambda function make function one liner
# it puts function into a variabel 
# practical usecase is when we have to pass a function as a argument then it is best.


