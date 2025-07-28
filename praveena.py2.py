import math
def operation():
    print("select the mathamatical function:")
    print("1:factorial")
    print("2:GCD")
    print("3:LCM")
    print("4:square") 
   
    x=int(input("Enter your choice:"))

    if x==1:
        a=int(input("Enter the number:"))
        print(f" factorial of a:{math.factorial(a)}")
    elif x==2:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        print(f" Greatest common division(GCD) of a and b:{math.gcd(a,b)}")
    elif x==3:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        print(f" Lcm of a and b:{math.lcm(a,b)}")



if __name__=="__main__" :
 operation()



