x = float(input()) # Must be greater than minimum error (10^-3)
x_p=0
counter=1
while (abs(x-x_p)>=10**(-3)): #iterates till error is less than 10^-3
    x_p=x
    x = (x+(2/x))/2
    print(x,counter) # prints x along with step number
    counter+=1