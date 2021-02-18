#regular expressions(re)
import re
text="A random string."
pattern=re.compile("A random string.")
result=pattern.search(text)
print(result)

pattern1=re.compile("[ABC]")
result1=pattern1.search(text)
print(result1)

pattern2=re.compile("[rskhvbsjdvhbakfvbh]")
result2=pattern2.search(text)
print(result2)
pattern3=re.compile("[a-z]")
result3=pattern3.search(text)
print(result3)

pattern4=re.compile("[a-zA-Z]")
result4=pattern4.search(text)
print(result4)

pattern3=re.compile("[a-zA-Z0-9]+")
result3=pattern3.search(text)
print(result3)

text1="jkrt.ngh69@gmail.com"
pattern5=re.compile("[a-z]+\.[a-z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
result5=pattern5.search(text1)
print(result5)

# \ escape 
text2="jkrt.ngh69@gmail.com , jkrt.ngh69@gmail.com, jaskirat409@gmail.com"
pattern6=re.compile("[a-z0-9\.\_\-]+\@[a-zA-Z0-9]+\.[a-zA-Z]+")
result6=pattern6.search(text2)
result=pattern6.findall(text2)
print(result)




