def add(a,b):
     return a + b
def subtract(a,b):
     return a - b
def multiply(a,b):
     return a * b
def divide(a,b):
     return a/b
def findrem(a,b):
     return a % b

def calculator():
     print("Welcome to Calculator App 🌈✨")
     print("Please Enter your Choice : 1.Addition  2.Subtraction  3.Multiplication  4.Division  5.Finding  Remainder ")
     while True:
          choice = input("Enter The operation to be performed:")
          if choice in ['1','2','3','4','5']:
            n1 = int(input("Enter operand 1 value:"))
            n2 = int(input("Enter operand 2 value:"))
            if choice == '1':
             print(f"{n1} + {n2} = {add(n1,n2)}")
            if choice == '2':
             print(f"{n1} - {n2} = {subtract(n1,n2)}")
            if choice == '3':
             print(f"{n1} * {n2} = {multiply(n1,n2)}")
            if choice == '4':
             print(f"{n1} / {n2} = {divide(n1,n2)}")
            if choice == '5':
             print(f"{n1} % {n2} = {findrem(n1,n2)}")
          next_calculation = input("Do you want to perform another calculation?")
          if next_calculation == 'y':
               break
calculator()         