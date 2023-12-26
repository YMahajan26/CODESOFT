# calculator
logo= '''
              _               _         _                
             | |             | |       | |               
  ___   __ _ | |  ___  _   _ | |  __ _ | |_   ___   _ __ 
 / __| / _` || | / __|| | | || | / _` || __| / _ \ | '__|
| (__ | (_| || || (__ | |_| || || (_| || |_ | (_) || |   
 \___| \__,_||_| \___| \__,_||_| \__,_| \__| \___/ |_|   
                                                                                                                     
'''
def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  try:
    return n1 / n2
  except ZeroDivisionError:
    print("Divide by Zero error!")

operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculator():
  print(logo)
  num1 = float (input("What's the first number: "))
  
  print("\nOperations: ")
  for symbol in operations:
    print(symbol,end="\t")

  conti=True
  while(conti):
    op=input("\n\nWhat operation do u want to perform? ")
    
    if op != '+' and op != '-' and op != '*' and op != '/':
      print("\nInvalid input.Choose correct option.")
      op=input("\nWhat operation do u want to perform? ")
      
    num2 = float (input("\nWhat's the next number:  "))
    cal_fun = operations[op]
    answer = cal_fun(num1,num2)
    print(f"{num1} {op} {num2} = {answer}")
    
    conti=input(f"\nType: \n1. 'y' to continue with {answer} or"
                f"\n2. 'c' to start new calculation or "
                f"\n3. 'n' to exit program"
                f"\nYour choice:  ")
    
    if conti == 'y':
      num1=answer
    elif conti=='c':
      conti=False
      calculator()
    else:
      conti = False

calculator()