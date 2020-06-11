file1 =  open("D:/Python/address1.txt","r")
file2 =  open("D:/Python/address2.txt","r")
file1 = file1.readlines()
file2 = file2.readlines()

dic1={}
dic2={}
for each in file1:
    each=each.strip()
    each=str(each[0:]).split('，')
    dic1[each[0]] = each[1]
for each in file2:
    each=each.strip()
    each=str(each[0:]).split('，')
    dic2[each[0]] = each[1]
    
#print(dic1)
#print(dic2)

for line in dic1:
    if line in dic2:
        dic1[line] = dic1[line]+"  "+dic2[line]
    else:
        dic1[line] = dic1[line]+"    "+"**********"

for line2 in dic2:
    if line2 not in dic1:
        dic2[line2] = "**********"+"  "+dic2[line2]

#print(dic2)
for i in dic2:
    if i not in dic1:
        dic1[i]=dic2[i]

print("姓名       电话        邮箱")
for line in dic1:
    print(line+"   "+dic1[line])


      
        
    



