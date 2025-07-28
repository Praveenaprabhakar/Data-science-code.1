import math
def basic_operation():
    a=int(input("Enter the number A:"))
    b=int(input("Enter the number B:"))
    print(f" addition(a+b):{a+b}")
    print(f" subtration(a-b):{a-b}")
    print(f" multiplication(a*b):{a*b}")
    print(f" division(a/b):{a/b}")
    print(f" floor devision(a//b):{a//b}")
    print(f" moduls(a%b):{a%b}")
    print(f" exponentation(a+b):{a+b}")


def advanced_math_function():
    print(f"/nSquare Root of(num):{math.sqre(num)}")
    print(f" factorial of 5:{math.factorial(5)}") 
print(f" Greatest common division(GCD) of 56 and 13:{math.gcd(56,13)}") 
print(f" Lcm of 23 and 45:{math.lcm(12,15)}")
print(f" absoluate value 0f -10:{math.fabs(-10)}") 
print(f" celling of 3.7:{math.ceil(3.7)}") 
print(f" Floor of 3.6:{math.floor(3.6)}") 
print(f" power of (3^5):{math.pow(3,5)}") 
print(f" logarithm(log(100)):{math.log(100)}") 
print(f" logarithm base 10(log 10(1000)):{math.log10(1000)}")
print(f" exponentation(e^7):{math.exp(7)}")


basic_operation()
advanced_math_function ()


