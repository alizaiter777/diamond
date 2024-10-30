x=int(input("Enter number of rows : "))
#first loop generates rows 
for i in range (x):
     #second loop prints * according to i 

     for j in range (i):
       
        print( "*" ,end="")
      
     print("")  

#generates rows in decreasing order which the second loop depends on i 
for i in range (x,0,-1):
     for j in range (i):
        print( "*" ,end="")
       
     print("")           
 

  