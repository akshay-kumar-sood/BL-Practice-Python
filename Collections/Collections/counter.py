from collections import Counter

number=[1,2,3,2,3,3,4,5,1,2]

count=Counter(number)
print(count.most_common())

name="Banana"
count=Counter(name)
print(count)

word=["java","python","c","cpp","rust","c#"]
count=Counter(word)
print(count)
print(type(count).__name__)


c=Counter("Apple")
c.update("Banana")
print(c)

c=Counter("Giving Up Is Not In THe Blood Sir")
c.subtract("SIr")
print(c)


word="giving up   is not   in the    blood sir"
counter=Counter(word.split())
print(f"Total word in string are : {len(counter)}")


# summary

# basically iska kaam hai count karna. 
# ek string doge letter(har character) kar dega. multiple string toh har ki frwquency kcount kar dega. int doge toh har ki frequency count kar dega
# kuch method hai jaise ki most_common(2)
#  kuch method hai jaise ki update to update value
# subtract agr kuch katn aho toh
# string me counter har character ko count karta hai. use split

# Counter(list) → List ke elements count karega.
# Counter(string) → String ke characters count karega.
# Counter(string.split()) → String ke words count karega.