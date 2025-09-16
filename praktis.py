"""
myList=[]
myList=["Raymundo","Lachica","Fiesta"," Repollo"]
print(myList)
myList[2]
myList[::-1]
myList[1:3:2]
myList.append("flores")
list="adarme", "paltep"
myList.append(list)
myList.insert(1, "John")

for x in myList:
   print(f"{x}", end=" ")
for y in range(len(myList)):
   print(f"{myList[y]}", end=" ")
   myList.pop()
   myList.pop(0)
   myList.remove("Lachica")
   list2=["Monje","Espiritu"]
   print(myList + list2)
   myList.sort()
   print(myList)
   myList.reverse
   print(myList)


myList2=[]
for x in range(3):
      print("Enter number: ")
      num1=float(input())
      myList2.append(num1)

nestedlist= [[12,5,3], [6.9,5]]
nestedlist=[[1] [0]]
nestedlist[[0] [1]]
for x in range(len(nestedlist[x])):
   print(f"{nestedlist[x],[y]}" end=" ") 
   """
"""
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print("\Enter scores: ")
for i in range(1, rows + 1):
   print(f"\nRow{i}")
   scores = []
for x in range(1, cols + 1):
   score = float(input(f"Enter score{x}: "))
   scores.append(score)
   total = sum(scores)
   average = total / cols
   print(f"Sum = {total}")
   print(f"Average = {average:.2f}")

for x in nestedlist:
    for y in x:
      print(f"{y}", end="")
   print()
   """
"""
   myTuple=(1,4,5,6)
   x=list(myTuple)
   x.append(8)
   x.append(70)
   x.rmeove(5)
   x.pop()

   myTuple=type(x)
   print(myTuple2)
   for x in myTuple2:
      print(x, end=" ")
      """

mydict={"id: ", "URDA-0011","name","velasco","salary: "}
mydict=["age"]="28"
mydict=["sex"]="male"
mydict=["name"]="Tugare"
mydict.popityem()
mydict.pop("name")