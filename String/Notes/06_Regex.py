# Regrex - python regular expression

#makes search, match and manipulate string easy short fast

# functions 
# 1. search() -> search first occurance of pattern
# 2. finall() -> search and return all matching  pattern. return list
# 3. 



import re

qoute="I scream, you scream, we all scream for ice cream."
result=re.search("scream",qoute)
print(result)

findall=re.findall("scream",qoute)
print(findall)

# special codes
# 1. \d --> any digit 0-9. 24 will turn to 2 and 4.
# r means raw string 
# 2. \d+ -> so that 24 appear as 24 not 2 and 4
# 3. D --> give other like spaces letter pancuation but not digit 

text="I have 2 apples and 5 oranges and 24 banana."
matched=re.findall(r"\d",text)
print(matched)

multi=re.findall(r"\d+",text)
print(multi)


non_digit=re.findall(r"\D",text)
print(non_digit)

# codes summary
# 1. \d -> digit form 0-9
# 2. \d+ -> digit 24 treat as 24 not 2 and 4
# 3. \D -> non digit
# 4. \w  ->  letternumbers underscore
# 5. \W  -> match special character space
# 6. \s -> match space newline tab
# 7  \[] -> search in range [0-9] [a-z] [a-zA-Z]
# 8. a* --> zero or more
# 9. ? => zero or one
# 10. {} --> exact no of time repitation
# 11. ^ --> start of string means search hello so in "hi hello" fails
# 12. $ --> end of string
# 13 | --> or operator 
# 14. dot --> represent as \.


email="akshay@gmail.com"
pattern=r"^[\w]+@+(gmail.com | yahoo.in)$ "