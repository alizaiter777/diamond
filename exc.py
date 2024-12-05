

x=int(input("Enter number of rows : "))
#first loop generates rows 
for i in range (x):
     #second loop prints * according to i 
     for j in range (x - i - 1): 
          print(" ", end="")  
          
     for k in range(2*i+1) :
          print( "*" ,end="")
     print()
      
    

for i in range (x,0,-1):
      for j in range (x - i - 1): 
          print(" ", end="")     
      for k in range(2*i+1) :
          print( "*" ,end="")
      print() 

 

  
