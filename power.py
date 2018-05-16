def inputNumber(message):
  while True:
    try:
       userInput = int(raw_input(message))       
    except ValueError:
       print("Invalid Input")
       continue
    else:
       return userInput 
       break 

x=inputNumber("");
y=inputNumber("");
z=x**y
print z