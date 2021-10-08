def isOperand(char) -> bool:
  if char in "123456789x":
    return True
  else:
    return False

def isOperator(char)  -> bool:
  """ Return True if the passed char is a operator """
  if char in "-+*/^(":
    return True
  else:
    return False

def isOpenParentheses(char) -> bool:
  """ If the passed char is '(', True is returned. Otherwise, False is returned."""
  if char == "(":
    return True
  else:
    return False

def isEmpty(listed) -> bool:
  """ Returns if a passed list is empty or not """
  if listed:
    return False
  else:
    return True

def operatorsComparison(op1, op2):
  """ 
    Return True if op2 is higher than op1. 
    Ex.: '^' is higher than '+' 
    Operators are organized on this order: - + * / ^ (
  """
  
  if not isOperator(op1) or not isOperator(op2):
      return "Error: 000033 - Missuse of comparison function"

  operator_order = ['+', '-', '*', '/', '^', '(']

  if operator_order.index(op2) > operator_order.index(op1):
    return True
  else:
    return False
    

def toPostfix(infix) -> str:
  stack = []
  postfix = ''

  for char in infix:
    print(stack)
    if isOperand(char):
        postfix += char

    elif isOperator(char):
      if isEmpty(stack): ## If stack is empty
        stack.append(char)

      elif operatorsComparison(stack[-1], char):
        ## In case char is higher than the top char on stack
        stack.append(char)

      else:
        ## In case the top char on stack is higher than char itself
        postfix += stack.pop()
        while(not isEmpty(stack)):
          if not operatorsComparison(stack[-1], char):
            postfix += stack.pop()
          else:
            break
        stack.append(char)
    
    elif char == ")":
      if isEmpty(stack):
        while not isOpenParentheses(stack[-1]):
          postfix += stack.pop()
        postfix += stack.pop()
      else:
        # This would only occur if a closing parentheses is used without being opened before.
        return "Error: 000061 - Bad parentheses use."
    else:
      return "Error: 000080 - Not expected value on expression."

  return postfix

print(toPostfix("2+5*x"))


