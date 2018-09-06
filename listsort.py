my_list = [2,0,6,5,1,7,'z','a']
even = []
odd = []
char = []
dictA ={}

for i in my_list:
    if isinstance(i,str):
        char.append(i) 
    elif i%2 == 0:
      even.append(i)
    else:
      odd.append(i)
dictA ['even'] = even 
dictA['odd'] = odd 
dictA['char'] = char      

print(even)
print(odd)
print(char)

print(dictA)
    
    

   
   
