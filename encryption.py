import string
az= string.ascii_lowercase
list1 = []
for i in az:
    list1.append(i)
kk=[]
phrase=input("Enter : \n")
v=phrase.lower()
empty=list(v)
for element in empty:
        if element in list1:
            kk.append(element)
pop = [list1.index(i) for i in kk]

change=[]
for i in range(len(pop)):
    change.append((pop[i]+3)%26)
final=[]
for i in range(len(change)):
    final.append(list1[change[i]])
print(''.join(str(e)for e in final))
