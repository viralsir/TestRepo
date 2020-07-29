import math;
no1=int(input("Enter No:"))
no2=int(input("Enter No:"))
no3=int(input("Enter No:"))

if no1>no2 and no1>no3:
    print(no1," is a maximum no");
elif no2>no1 :
    print(no2," is a maximum no");
else :
    print(no3," is a maximum no");

print("Factorial :",math.factorial(no2));
