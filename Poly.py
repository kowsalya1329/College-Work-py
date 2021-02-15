values=[int(input("Coeff:")) for i in range(0,int(input("Enter degree")))]
cons=(int(input("Const:")))
values.append(cons)
print("Ploynomial to be writen :")
#print(values)
fin_list=values[::-1]

temp_list=[]
for i in range(len(fin_list)-1,0,-1):
    if fin_list[i]!=0 & i-1==0:
        if fin_list[i]>0:
            rs= "+" +str (fin_list[i])+"x^"+str (i)
            temp_list.append(rs)
        else:
            rs= str (fin_list[i])+"x^"+str (i)
            temp_list.append(rs)

if cons>0:
    es="+"+str (cons)
    temp_list.append(es)
else:
    temp_list.append(cons)





s="".join(str(x) for x in temp_list)
print(s)