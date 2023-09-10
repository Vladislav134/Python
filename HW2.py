data = [int(i) for i in input('Введите числа через пробел: ').split()]
n = len(data)
count1 = 0
count2 = 0    
for i in data:
    if i==1:
       count1 +=1
    else:
        if i==0:
         count2 +=1
if count1 < count2:
   i = 0
   print(count1)
else:
   i = 1
   print(count1)  
   print(0)        
    

