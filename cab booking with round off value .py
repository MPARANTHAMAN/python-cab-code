source=0
print("enter the destination")
destination=input()

if(destination.isalpha()):  
   print("invalid statement")
else :   
  total=float(destination)+0  
  print("total distance",total) 
  print(round(total,0))        
  print("press 1 for auto")
  print("press 2 for mini")
  print("press 3 for maxi")
choice=int(input("my choice="))

if(float(choice)==1):
    auto=4*total
    print("your  auto price:",auto)
    print("round off auto price ",round(auto,0)) 
elif(float(choice)==2):
  mini=10*total
  print("your  mini price is",mini)
  print("round off mini price",round(mini,0))
  
elif(float(choice)==3):
    maxi=15*total
    print("your maxi price is",maxi)
    print("round off maxi price ",round(maxi,0)) 
else :
	  print("invalid")
