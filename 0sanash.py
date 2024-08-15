from os import system
system("cls")

strr= input("Sonni kiriting: ")
count = 0
for i in strr:
   if i in "00":
      count += 1
   else:
      break
print(count)
