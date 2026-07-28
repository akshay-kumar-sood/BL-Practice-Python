import myCalculator

first_num=int(input("Enter first number : "))
second_num=int(input("Enter second number : "))

res_add=myCalculator.add(first_num,second_num)
print("Addition is : ",res_add)

res_sub=myCalculator.sub(first_num,second_num)
print("differnce is : ",res_sub)

res_mul=myCalculator.multiply(first_num,second_num)
print("product: ",res_mul)

res_div=myCalculator.divide(first_num,second_num)
print("divide: ",res_div)


