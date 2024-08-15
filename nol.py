from os import system
from json import dumps
system("cls")

s1 = int(input("Sonni kiriting: "))
dct = {}
son = str(s1)
lst= list(son)
lst.sort()
for sonlar in lst:
   dct[sonlar] = lst.count(sonlar)
   
print(dumps(dct,indent=4))
