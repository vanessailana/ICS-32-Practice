#function to perform calculations based on user input

def calculate(operand1,operand2,operator):

  try:
    if operator =='+':
      return operand1+operand2
    elif operator =='-':
      return operand1 - operand2
    elif operator == 'x':
      return operand1 * operand2

    elif operator=='/':
      if operand2== 0:
        raise ZeroDivisionError("Not allowed")

      return operand1/ operand2

    else:
      raise ValueError("Invalid")

  except ZeroDivisionError as e:
            return str(e)


  except ValueError as e:
        return str(e)


try:
  print("Enter the first operand")
  operand1=float(input())
  print("Enter the second operand")
  operand2=float(input())
  print("Enter the desired operator")
  operator=input()

  result=calculate(operand1,operand2,operator)

  print(result)

except ValueError:
  print("Wrong, please enter valid numeric operands")
