import numpy as np
A1=np.array([21,1,3,1,0])
A2=np.array([41,2,1,0,1])
A3=np.array([25,1,6,0,1])
A4=np.array([17,2,12,1,0])
A5=np.array([30,1,3,0,1])
values=[A1,A2,A3,A4,A5]
empty=[]
for i in range(0,len(values)):
    for j in range(0,len(values)):
        sum_ij=sum(values[i]*values[j])
        sum_ii=sum(values[i]*values[i])
        sum_jj=sum(values[j]*values[j])
        J=sum_ij/((sum_ii)+(sum_jj)-(sum_ij))
        print("J(A"+str(i+1)+",A"+str(j+1)+")="+str(J))
        empty.append(J)
    least=min(empty)
    pos=empty.index(least)
    print(pos)
    print("The recommendation for A"+str(i+1)+" is A"+str(pos+1))