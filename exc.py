nbr_of_rows=int(input("Enter number of rows : "))
#first loop generates rows 
for i in range (nbr_of_rows):
     #second loop prints * according to i 

     for j in range (i):
       
        print( "*" ,end="")
      
     print("")  

#generates rows in decreasing order which the second loop depends on i 
for i in range (nbr_of_rows,0,-1):
     for j in range (i):
        print( "*" ,end="")
       
     print("")           
 

  
