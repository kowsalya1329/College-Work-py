Numbers=[0, 5, 0, -4, 2, 3, -2, 8, 4]
digits=len(Numbers)-1
power_of=digits
polynomial_nums=""

for i in Numbers:
   if power_of>0 and power_of==int(digits) and i>0 and i!=1:
     polynomial_nums=polynomial_nums+str(i)+'x^'+str(power_of)
     power_of=power_of-1
   elif power_of>0 and power_of==int(digits) and i>0 and i==1:
     polynomial_nums=polynomial_nums+'x^'+str(power_of)
     power_of=power_of-1
   elif power_of>0 and power_of==int(digits) and i<0 and i==-1:
     polynomial_nums=polynomial_nums+'-x^'+str(power_of)
     power_of=power_of-1
   elif power_of>0 and power_of==int(digits) and i<0 and i!=-1:
     polynomial_nums=polynomial_nums+'x^'+str(power_of)
     power_of=power_of-1
   elif power_of>0 and power_of==int(digits) and i==0:
     polynomial_nums=polynomial_nums
     power_of=power_of-1
     
   elif power_of>0 and power_of+1==int(digits) and Numbers[0]==0 and i>0 and i!=1:
     polynomial_nums=polynomial_nums+str(i)+'x^'+str(power_of)
     power_of=power_of-1
   elif power_of>0 and power_of+1==int(digits) and Numbers[0]==0 and i>0 and i==1:
     polynomial_nums=polynomial_nums+'x^'+str(power_of)
     power_of=power_of-1
     
   elif power_of>0 and power_of!=1 and power_of!=int(digits) and i>0 and i!=1:
     polynomial_nums=polynomial_nums+' +'+str(i)+'x^'+str(power_of)
     power_of=power_of-1
   elif power_of>0 and power_of==1 and power_of!=int(digits) and i>0 and i!=1:
     polynomial_nums=polynomial_nums+' +'+str(i)+'x'
     power_of=power_of-1
   elif power_of>0 and power_of!=1 and power_of!=int(digits) and i>0 and i==1:
     polynomial_nums=polynomial_nums+' +'+'x^'+str(power_of)
     power_of=power_of-1
   elif power_of>0 and power_of==1 and power_of!=int(digits) and i>0 and i==1:
     polynomial_nums=polynomial_nums+' +'+'x'
     power_of=power_of-1
   elif power_of>0 and power_of!=1 and power_of!=int(digits) and i<0 and i!=-1:
     polynomial_nums=polynomial_nums+' '+str(i)+'x^'+str(power_of)
     power_of=power_of-1
   elif power_of>0 and power_of==1 and power_of!=int(digits) and i<0 and i!=-1:
     polynomial_nums=polynomial_nums+' '+str(i)+'x'
     power_of=power_of-1
   elif power_of>0 and power_of!=1 and power_of!=int(digits) and i<0 and i==-1:
     polynomial_nums=polynomial_nums+' -x^'+str(power_of)
     power_of=power_of-1
   elif power_of>0 and power_of==1 and power_of!=int(digits) and i<0 and i==-1:
     polynomial_nums=polynomial_nums+' -x'
     power_of=power_of-1
   elif power_of>0 and power_of!=int(digits) and i==0:
     polynomial_nums=polynomial_nums
     power_of=power_of-1
   elif power_of==0 and power_of!=int(digits) and i>0:
     polynomial_nums=polynomial_nums+' +'+str(i)
     power_of=power_of-1
   elif power_of==0 and power_of!=int(digits) and i<0:
     polynomial_nums=polynomial_nums+' '+str(i)
     power_of=power_of-1
   else:
     polynomial_nums=polynomial_nums
     break
   
print(polynomial_nums)