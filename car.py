source=1
print("enter the desigination")
desigination=int(raw_input())
total=desigination+1
print("press 1 for auto")
print("press 2 for mini")
print("press 3 for maxi")
choice=int(raw_input("my choice="))
if(choice==1):
	auto=4*total
	print("you  auto price:",auto)
elif(choice==2):
	mini=10*total
	print("you  mini price is",mini)
elif(choice==3):
    maxi=15*total
    print("you maxi price is",maxi)
else :
	print("invalid")
