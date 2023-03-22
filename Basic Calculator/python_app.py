# define the functions needed: add, sub, mul, div
# Print options to the user 
# ask for values
# call the functions
# while loop to continue the program until the user wants to exit

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a,b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer)+ "\n")

def mul(a,b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer)+ "\n")

def div(a,b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer)+ "\n")

while True:
    print("A. addition")
    print("B. subtraction")
    print("C. multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("input your choice: ")

    if choice == "e" or choice == "E":
        print("program ended")
        quit()
    else:
        a = int(input("input first number: "))
        b = int(input("input second number: "))

        if choice == "a" or choice == "A":
            add(a, b)
        elif choice == "b" or choice == "B":
            sub(a,b)
        elif choice == "c" or choice == "C":
            mul(a,b)
        elif choice == "d" or choice == "D":
            div(a,b)
   