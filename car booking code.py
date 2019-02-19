source=0
print("enter the destination")
destination=raw_input()
if(destination)<=1:
   print("invalid statement")
elif(destination.isalpha()):  
   print("invalid statement")
else :   
  total=float(destination)+0
print("total distance",total)  
print("press 1 for auto")
print("press 2 for mini")
print("press 3 for maxi")
choice=int(raw_input("my choice="))
if(float(choice)==1):
	auto=4*total
	print("you  auto price:",auto)
elif(float(choice)==2):
	mini=10*total
	print("you  mini price is",mini)
elif(float(choice)==3):
    maxi=15*total
    print("you maxi price is",maxi)
else :
	print("invalid")
