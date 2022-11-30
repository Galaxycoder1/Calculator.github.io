def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Choose operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Area Of square")
print("6.Perimeter of circle")
print("7.Area of Square")
print("8.Perimeter of Square")
print("9.Area of Rectangle")
print("10.Perimeter of Rectangle")
print("11.Perimeter of ")


while True:

    print("  ")
  
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):

        print("  ")
      
        if choice == '1':
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number: "))
            print(num1, "+", num2, "=", add(num1, num2))
            print("  ")

        elif choice == '2':
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number: "))
            print(num1, "-", num2, "=", subtract(num1, num2))
            print("  ")

        elif choice == '3':
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number: "))
            print(num1, "*", num2, "=", multiply(num1, num2))
            print("  ")

        elif choice == '4':
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number: "))
            print(num1, "/", num2, "=", divide(num1, num2))
            print("  ")

        elif choice == '5':
            radius = float(input("Radius:   "))
            pi = 3.141592653589793238
            print("𝝅r2 =", pi*radius*radius)
            print("   ")

        elif choice == '6':
            radius = float(input("Radius:   "))
            pi = 3.141592653589793238
            print("2𝝅r =", 2*pi*radius)
            print("  ")

        elif choice == '7':
            side = float(input("Side:   "))
            print("s*s =", side*side)
            print("  ")
          
        elif choice == '8':
            side = float(input("Side:   "))
            print("4s =", 4*side)
            print("  ")

        elif choice == '9':
            l = float(input("Length :   "))
            b = float(input("Breadth:   "))
            print("l*b =", l*b)
            print("  ")
        elif choice == '10':
            l = float(input("Length :   "))
            b = float(input("Breadth:   "))
            a = 2
            print("2(l+b) =", a*l+a*b)
            print("   ")
          
        next_calculation = input("Let's do next calculation? (y/n): ")
        if next_calculation == "n":
          break
    
    else:
        print("Invalid Input")
