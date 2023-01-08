#for c in range(1,51):   
     #if c % 2 == 0:  
        #print (c)
        
#Essa maneira acima exige muito do prpcessador. O ideal é fazer assim:

for c in range(2,51,2):
    print (c,end=" ")                