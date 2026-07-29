# PROG 4: Count Character In The String

# Write The Code Here
def count_char(str):
  lower_str=str.lower()
  count={}

  for char in lower_str:
    if char.isalnum():
      if char in count:
        count[char]+=1
      else:
        count[char]=1
  return count


str=input("Input String :")

res=count_char(str) 

print(f"Character Count : {res}")


