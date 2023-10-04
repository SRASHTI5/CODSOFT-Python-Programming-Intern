import random
comp=random.randint(1,3)
user=int(input("Enter 1 for Stone\nEnter 2 for Paper\nEnter 3 for Scissor\n "))
def result(comp,user):
    if(comp==user):
        return 0
    if(comp==3 and user==2):
        return -1
    if(comp==1 and user==3):
        return -1
    if(comp==2 and user==1):
        return -1
    else:
        return 1
result=result(comp,user)
print("You: ",user)
print("Computer:",comp)
if(result==0):
    print("It's a DRAW")
elif(result==-1):
    print("You LOSE")
else:
    print("You WON!")