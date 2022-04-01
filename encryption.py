import string
az= string.ascii_uppercase
list1 = []
list1.append(" ")
for i in az:
    list1.append(i)
phrase_list=[]
phrase=input("Enter phrase : \n")
change_upper=phrase.upper()
entered_phrase=list(change_upper)
for element in entered_phrase:
        if element in list1:
            phrase_list.append(element)
Locate=[list1.index(i) for i in phrase_list]

change=[]
for i in range(len(Locate)):
    change.append((Locate[i]+4)%27)
final=[]
for i in range(len(change)):
    final.append(list1[change[i]])
print(''.join(str(e)for e in final))
