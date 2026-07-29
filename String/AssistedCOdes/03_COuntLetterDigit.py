# PROG 3.1: Counting Letters, Digits, and Special Symbols in a String Using Explicit Loops

# Write The Code Here

def count_char(str):
  alpha_cnt=0
  digit_cnt=0
  special_cnt=0

  for i in range(0,len(str)):
    if str[i].isalpha():
      alpha_cnt+=1
    elif str[i].isdigit():
      digit_cnt+=1
    else:
      special_cnt+=1

  return alpha_cnt,digit_cnt,special_cnt

str="P@hsks#slsk11nsjs"
print(f"Input string is : {str}")
alpha,digit,special=count_char(str)

print(f"Number of letters : {alpha}")
print(f"Number of letters : {digit}")
print(f"Number of letters : {special}")


# when a python file run 
# __name__ = "__main__"
# when we do impprt any file
# then main does not run and __name__ set to that imported file 
# __name__="Calculator"

