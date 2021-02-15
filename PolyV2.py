fin_list=[2,3,-4,5,-5,5]
temp_list=[]
for i in range(len(fin_list)-1,0,-1):
    if fin_list[i]!=0 & i-1==0 :
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





s=" ".join(str(x) for x in temp_list)
print(s)