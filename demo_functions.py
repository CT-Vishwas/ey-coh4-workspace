M = 100
N = 75

def display_menu():
    print("\n-------Calculator-----------\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Quit")

def add(a,b):
    global M
    print(f"Value of M on line 8 inside add:{M}")
    M = 25
    print(f"Value of M inside add:{M}")
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


display_menu()
choice = int(input("Enter the choice: "))
a = float(input("Enter first Number: "))
b = float(input("Enter second Number: "))

if choice == 1:
    print(f"{a}+{b} = {add(a,b)}")
    print(f"Value of M on 31:{M}")
elif choice == 2:
    print(f"{a}-{b} = {sub(a,b)}")
elif choice == 3:
    print(f"{a}*{b} = {mul(a,b)}")
elif choice == 4:
    print(f"{a}/{b} = {div(a,b)}")
elif choice == 5:
    exit(0)
else:
    print("Invalid Choice")

print(f"Value of M on lin3 38:{M}")